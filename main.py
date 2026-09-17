import http.server
import socketserver
import webbrowser
import threading

PORT = 8080

# Database expanded with 30+ top tools
ai_tools_database = {
    "Video Editors": {
        "CapCut Web": "https://www.capcut.com",
        "Wondershare Filmora": "https://filmora.wondershare.com",
        "Clipchamp": "https://clipchamp.com",
        "VN Video Editor": "https://vlognow.me",
        "DaVinci Resolve": "https://www.blackmagicdesign.com/products/davinciresolve",
        "Premiere Pro": "https://www.adobe.com/products/premiere.html",
        "Runway (AI Video)": "https://runwayml.com",
        "Pika Labs": "https://pika.art",
        "HeyGen": "https://www.heygen.com"
    },
    "AI Assistants": {
        "Gemini": "https://gemini.google.com",
        "ChatGPT": "https://chatgpt.com",
        "Claude": "https://claude.ai",
        "Perplexity AI": "https://www.perplexity.ai",
        "Microsoft Copilot": "https://copilot.microsoft.com",
        "Poe": "https://poe.com",
        "HuggingChat": "https://huggingface.co/chat/"
    },
    "Graphics & Design": {
        "Canva Magic Studio": "https://www.canva.com",
        "Midjourney": "https://www.midjourney.com",
        "DALL-E 3": "https://openai.com/dall-e-3",
        "Leonardo.ai": "https://leonardo.ai",
        "Adobe Firefly": "https://firefly.adobe.com",
        "Figma AI": "https://www.figma.com",
        "Picsart AI": "https://picsart.com"
    },
    "Audio & Music": {
        "ElevenLabs": "https://elevenlabs.io",
        "Suno AI": "https://suno.com",
        "Udio": "https://www.udio.com",
        "Murf AI": "https://murf.ai",
        "LALAL.AI": "https://www.lalal.ai"
    },
    "Coding & Study": {
        "GitHub Copilot": "https://github.com/features/copilot",
        "Cursor (AI Editor)": "https://www.cursor.com",
        "Gamma": "https://gamma.app",
        "QuillBot": "https://quillbot.com",
        "Notion AI": "https://www.notion.so/product/ai",
        "Blackbox AI": "https://www.blackbox.ai"
    }
}

class WebHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # HTML aur CSS with Top Navigation Bar aur Anchor Links
        page = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>The Student Logical World</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
                
                html {
                    scroll-behavior: smooth;
                    scroll-padding-top: 90px; /* Navbar ke neeche scrolling set karne ke liye */
                }

                body { 
                    font-family: 'Poppins', sans-serif; 
                    background: #111111; 
                    color: #ffffff; 
                    margin: 0; 
                    padding: 0;
                }
                
                /* 1. Navbar Design (Like The Dada's Mehfil) */
                nav {
                    position: fixed;
                    top: 0;
                    width: 100%;
                    background: rgba(15, 15, 15, 0.95);
                    backdrop-filter: blur(10px);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 15px 40px;
                    box-sizing: border-box;
                    z-index: 1000;
                    border-bottom: 1px solid #333;
                }

                .logo {
                    font-size: 22px;
                    font-weight: 800;
                    color: #00ffff;
                    letter-spacing: 1px;
                }

                .nav-links {
                    display: flex;
                    gap: 25px;
                }

                .nav-links a {
                    color: #fff;
                    text-decoration: none;
                    font-size: 16px;
                    font-weight: 600;
                    transition: 0.3s;
                }

                .nav-links a:hover {
                    color: #00ffff;
                }

                .btn-call {
                    background: #ff9f43;
                    color: #111 !important;
                    padding: 8px 20px;
                    border-radius: 25px;
                    font-weight: 800;
                }

                /* 2. Hero Section & Title */
                .hero {
                    margin-top: 100px;
                    text-align: center;
                    padding: 40px 20px;
                }

                @keyframes neonGlow {
                    0% { text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff; }
                    100% { text-shadow: 0 0 20px #ff00ff, 0 0 30px #ff00ff; }
                }
                
                h1.main-title { 
                    font-size: 55px; 
                    font-weight: 800;
                    letter-spacing: 2px;
                    margin: 0;
                    animation: neonGlow 2s infinite alternate;
                }

                /* 3. Top Highlights (Sirf Top 3 Tools) */
                .top-highlights {
                    display: flex;
                    justify-content: center;
                    gap: 30px;
                    padding: 40px;
                    flex-wrap: wrap;
                }

                .highlight-card {
                    background: linear-gradient(145deg, #1e1e1e, #2a2a2a);
                    padding: 30px;
                    border-radius: 15px;
                    width: 250px;
                    text-align: center;
                    border: 1px solid #444;
                    box-shadow: 0 10px 20px rgba(0,0,0,0.5);
                }

                .highlight-card h3 { color: #f9ca24; margin-top: 0; }
                .highlight-card a {
                    display: inline-block;
                    margin-top: 15px;
                    padding: 10px 20px;
                    background: #00ffff;
                    color: #111;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                }

                /* 4. Explore Button */
                .explore-container {
                    text-align: center;
                    margin-bottom: 60px;
                }

                .explore-btn {
                    background: transparent;
                    color: #00ffff;
                    border: 2px solid #00ffff;
                    padding: 15px 40px;
                    font-size: 18px;
                    font-weight: bold;
                    border-radius: 30px;
                    cursor: pointer;
                    text-decoration: none;
                    transition: 0.3s;
                }

                .explore-btn:hover {
                    background: #00ffff;
                    color: #111;
                    box-shadow: 0 0 15px #00ffff;
                }

                /* 5. All Tools Grid Section */
                .section-container {
                    padding: 40px 60px;
                }

                .section-title {
                    font-size: 30px;
                    color: #00ffff;
                    border-bottom: 2px solid #333;
                    padding-bottom: 10px;
                    margin-bottom: 30px;
                }

                .grid { 
                    display: grid; 
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
                    gap: 20px; 
                    margin-bottom: 60px;
                }
                
                .tool-link { 
                    display: block; 
                    background-color: #1e1e1e; 
                    color: #f5f6fa; 
                    padding: 15px 20px; 
                    text-decoration: none; 
                    border-radius: 10px; 
                    font-size: 16px;
                    font-weight: 600;
                    border: 1px solid #333; 
                    transition: 0.3s; 
                    text-align: center;
                }
                
                .tool-link:hover { 
                    background-color: #2c2c2c;
                    border-color: #ff9f43; 
                    color: #ff9f43;
                    transform: translateY(-5px);
                }
            </style>
        </head>
        <body>
            <!-- Navigation Bar -->
            <nav>
                <div class="logo">LOGICAL WORLD</div>
                <div class="nav-links">
                    <a href="#">Home</a>
                    <a href="#section-Video_Editors">Video Editors</a>
                    <a href="#section-AI_Assistants">AI Tools</a>
                    <a href="#section-Graphics_&_Design">Design</a>
                    <a href="#section-Coding_&_Study">Coding</a>
                    <a href="#all-tools" class="btn-call">Explore All</a>
                </div>
            </nav>

            <!-- Hero Section -->
            <div class="hero">
                <h1 class="main-title">THE STUDENT LOGICAL WORLD</h1>
                <p style="font-size: 20px; color: #aaa;">World's Top AI Tools & Workspaces for Students</p>
            </div>

            <!-- Top 3 Highlights -->
            <div class="top-highlights">
                <div class="highlight-card">
                    <h3>Gemini</h3>
                    <p>Advanced Research & Python Coding.</p>
                    <a href="https://gemini.google.com" target="_blank">Open Tool</a>
                </div>
                <div class="highlight-card">
                    <h3>CapCut Web</h3>
                    <p>Fast Video Editing & Auto Captions.</p>
                    <a href="https://www.capcut.com" target="_blank">Open Tool</a>
                </div>
                <div class="highlight-card">
                    <h3>Canva Studio</h3>
                    <p>Pro Thumbnails & Graphic Design.</p>
                    <a href="https://www.canva.com" target="_blank">Open Tool</a>
                </div>
            </div>

            <!-- Explore Button -->
            <div class="explore-container">
                <a href="#all-tools" class="explore-btn">Explore All AI Tools & Editors 👇</a>
            </div>

            <!-- Complete Database Generation (Dynamically) -->
            <div id="all-tools" class="section-container">
        """

        # Python dictionary se saare sections aur tools dynamically HTML me daalna
        for category, tools in ai_tools_database.items():
            safe_id = category.replace(" ", "_")
            page += f"<h2 id='section-{safe_id}' class='section-title'>{category}</h2><div class='grid'>"
            for name, link in tools.items():
                page += f"<a href='{link}' target='_blank' class='tool-link'>{name}</a>"
            page += "</div>"

        page += """
            </div>
        </body>
        </html>
        """
        self.wfile.write(page.encode("utf-8"))

def start_server():
    with socketserver.TCPServer(("", PORT), WebHandler) as httpd:
        httpd.serve_forever()

threading.Thread(target=start_server, daemon=True).start()
webbrowser.open(f"http://localhost:{PORT}")
print(f"🚀 THE STUDENT LOGICAL WORLD is live at: http://localhost:{PORT}")

input("Server is running... Press ENTER in this terminal to stop.\n")