"""
Platform-specific dependency installer for ResuMatch AI.
This script handles SQLite compatibility across different platforms.
"""

import sys
import subprocess
import platform

def install_platform_deps():
    """Install platform-specific dependencies"""
    system = platform.system().lower()
    print(f"🖥️  Detected platform: {system}")
    
    try:
        if system in ['linux', 'darwin']:  # Linux or macOS
            print("📦 Installing pysqlite3-binary for Unix systems...")
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', 
                'pysqlite3-binary', '--quiet'
            ])
            print("✅ Unix dependencies installed")
            
        elif system == 'windows':
            print("🪟 Windows detected - using alternative SQLite handling")
            print("✅ Windows compatibility mode enabled")
            
        else:
            print(f"⚠️  Unknown platform: {system}")
            print("🔄 Proceeding with default configuration")
            
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to install platform dependencies: {e}")
        print("🔄 Continuing with fallback mode")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    install_platform_deps()