import os

files_to_update = [
    "index.html",
    "managed-it-services-burlington.html",
    "managed-it-services-hamilton.html",
    "managed-it-services-guelph.html",
    "managed-it-services-waterloo.html",
    "managed-it-services-cambridge.html",
    "managed-it-services-kitchener-waterloo.html"
]

cwd = '/data/msp-site'

old_ms_logo = """    <!-- Microsoft -->
    <div class="partner-item" title="Microsoft">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 23 23" width="40" height="40">
        <rect x="1" y="1" width="10" height="10" fill="#f25022"/>
        <rect x="12" y="1" width="10" height="10" fill="#7fba00"/>
        <rect x="1" y="12" width="10" height="10" fill="#00a4ef"/>
        <rect x="12" y="12" width="10" height="10" fill="#ffb900"/>
      </svg>
    </div>"""

# Replace Microsoft logo with a grayscale/monochrome version to match the monochrome scheme of the other 3
new_ms_logo = """    <!-- Microsoft -->
    <div class="partner-item" title="Microsoft">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="36" height="36" fill="#fff" opacity="0.8">
        <path d="M11.4 24H0V12.6h11.4V24ZM24 24H12.6V12.6H24V24ZM11.4 11.4H0V0h11.4v11.4ZM24 11.4H12.6V0H24v11.4Z"/>
      </svg>
    </div>"""

old_google_logo = """    <!-- Google Workspace -->
    <div class="partner-item" title="Google Workspace">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="38" height="38">
        <path d="M21.8 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.5a4.7 4.7 0 0 1-2 3.1v2.5h3.3c1.9-1.8 3-4.4 3-7.4z" fill="#4285F4"/>
        <path d="M12 22c2.7 0 5-0.9 6.7-2.4l-3.3-2.5c-.9.6-2.1 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3v2.6A10 10 0 0 0 12 22z" fill="#34A853"/>
        <path d="M6.4 14c-.2-.6-.3-1.3-.3-2s.1-1.4.3-2V7.4H3A10 10 0 0 0 2 12c0 1.6.4 3.2 1 4.6L6.4 14z" fill="#FBBC05"/>
        <path d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.8-2.8A10 10 0 0 0 3 7.4L6.4 10c.8-2.3 3-3.9 5.6-4.1z" fill="#EA4335"/>
      </svg>
    </div>"""

# Replace Google logo with a grayscale/monochrome version to match the scheme
new_google_logo = """    <!-- Google Workspace -->
    <div class="partner-item" title="Google Workspace">
      <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="#fff" opacity="0.8">
        <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
        <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
        <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
        <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
      </svg>
    </div>"""

for filename in files_to_update:
    filepath = os.path.join(cwd, filename)
    if not os.path.exists(filepath):
        print(f"[!] File not found: {filename}")
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    if old_ms_logo in content:
        content = content.replace(old_ms_logo, new_ms_logo)
        print(f"[+] Replaced Microsoft logo in: {filename}")
        
    if old_google_logo in content:
        content = content.replace(old_google_logo, new_google_logo)
        print(f"[+] Replaced Google logo in: {filename}")
        
    with open(filepath, 'w') as f:
        f.write(content)

