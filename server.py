import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import guard

HOST = "127.0.0.1"  # this machine only; the server spends your Groq quota
PORT = int(os.getenv("PORT", "8000"))
INDEX = Path(__file__).parent / "index.html"
MAX_PROMPT_CHARS = 2000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Only the page itself is served, never the project folder (it holds .env).
        if self.path in ("/", "/index.html"):
            self.reply(200, INDEX.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/health":  # lets the page tell this server apart from a static host
            self.reply_json(200, {"ok": True})
        else:
            self.reply_json(404, {"error": "Not found"})

    def do_POST(self):
        if self.path != "/api/check":
            return self.reply_json(404, {"error": "Not found"})
        # Requiring JSON blocks other websites from firing blind requests at this server.
        if self.headers.get_content_type() != "application/json":
            return self.reply_json(415, {"error": "Send JSON"})
        try:
            length = int(self.headers.get("Content-Length", 0))
        except ValueError:
            return self.reply_json(400, {"error": "Bad Content-Length"})
        if length > 16 * 1024:
            return self.reply_json(413, {"error": "Request too large"})
        try:
            prompt = json.loads(self.rfile.read(length))["prompt"]
        except (ValueError, KeyError, TypeError):
            return self.reply_json(400, {"error": "Expected JSON like {\"prompt\": \"...\"}"})
        if not isinstance(prompt, str) or not prompt.strip():
            return self.reply_json(400, {"error": "Enter a prompt to check"})
        if len(prompt) > MAX_PROMPT_CHARS:
            return self.reply_json(400, {"error": f"Prompt is too long (max {MAX_PROMPT_CHARS} characters)"})
        self.reply_json(200, guard.check(prompt))

    def reply_json(self, status, data):
        self.reply(status, json.dumps(data).encode(), "application/json")

    def reply(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Prompt Guard running at http://{HOST}:{PORT}  (Ctrl+C to stop)")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
