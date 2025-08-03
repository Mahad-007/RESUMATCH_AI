# 📄 ResuMatch AI - Resume Gap Analyzer & Enhancer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)](https://crewai.com/)

A powerful AI-driven tool that analyzes your resume against job descriptions to identify gaps and provide actionable suggestions for improvement. Built with CrewAI agents and powered by Groq's fast inference.

## 🚀 Features

- **🔍 Resume Gap Analysis**: Identifies missing skills, experiences, and keywords between your resume and target job descriptions
- **✨ AI-Powered Suggestions**: Provides specific, actionable recommendations to improve your resume
- **📋 Multiple Format Support**: Works with both PDF and DOCX resume formats
- **🤖 Multi-Agent System**: Uses specialized AI agents for analysis and enhancement
- **⚡ Fast Processing**: Powered by Groq's high-performance LLM inference
- **🌐 Web Interface**: Clean, intuitive Streamlit-based user interface

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key (sign up at [groq.com](https://groq.com))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/resumatch_ai.git
   cd resumatch_ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
   # Optional: Install platform-specific SQLite compatibility
   python install_deps.py
   ```

3. **Environment Configuration**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🎯 Usage

1. **Start the application**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload your resume** (PDF or DOCX format)

4. **Paste the job description** you're targeting

5. **Click "Analyze Resume"** to get:
   - Identified gaps between your resume and the job requirements
   - Specific suggestions for improving your resume

## 🏗️ Architecture

### Core Components

- **`main.py`**: Streamlit web application interface
- **`agents/resume_agents.py`**: AI agents configuration
  - Resume Gap Analyzer Agent
  - Resume Enhancer Agent
- **`logic/resume_analyzer.py`**: Core analysis logic and text extraction
- **`sqlite_fix.py`**: SQLite compatibility module for ChromaDB
- **`chromadb_fix.py`**: ChromaDB initialization with error handling
- **`install_deps.py`**: Platform-specific dependency installer
- **`packages.txt`**: System dependencies for deployment

### AI Agents

The system uses two specialized CrewAI agents:

1. **Resume Gap Analyzer**
   - Role: Identifies skill, keyword, and experience mismatches
   - Goal: Find gaps between resume and job description
   - Expertise: Career consulting and requirement analysis

2. **Resume Enhancer**
   - Role: Optimize resume sections for ATS and hiring managers
   - Goal: Rewrite content to align with job requirements
   - Expertise: Resume optimization and ATS compliance

## 🔧 Technical Details

### Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Web application framework |
| `crewai` | Multi-agent AI system |
| `groq` | Fast LLM inference |
| `pdfplumber` | PDF text extraction |
| `docx2txt` | Word document processing |
| `python-dotenv` | Environment variable management |

### Supported File Formats

- **PDF**: Full text extraction with layout preservation
- **DOCX**: Microsoft Word document processing

## 🚦 Getting Started

### Quick Start Example

```python
from logic.resume_analyzer import analyze_resume_and_role

# Analyze resume against job description
gaps, suggestions = analyze_resume_and_role(resume_file, job_description)
print("Gaps:", gaps)
print("Suggestions:", suggestions)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://crewai.com/) for the multi-agent framework
- [Groq](https://groq.com/) for fast LLM inference
- [Streamlit](https://streamlit.io/) for the web framework

## 🚀 Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://share.streamlit.ioapp.com/)
3. The `packages.txt` file will ensure system dependencies are installed
4. Add your `GROQ_API_KEY` in the Streamlit Cloud secrets

### Other Platforms
For Heroku, Railway, or other platforms, ensure you:
- Set the `GROQ_API_KEY` environment variable
- The `pysqlite3-binary` package in requirements.txt handles SQLite compatibility
- The `sqlite_fix.py` module automatically resolves ChromaDB SQLite version issues

### Troubleshooting

#### SQLite Version Error
If you encounter: `RuntimeError: Your system has an unsupported version of sqlite3`

**Multi-Platform Solution**: The codebase includes comprehensive fixes:

1. **Automatic Detection**: `sqlite_fix.py` detects your SQLite version
2. **Platform-Specific Handling**: 
   - **Linux/Mac**: Uses `pysqlite3-binary` if available
   - **Windows**: Uses environment variable overrides and patches
3. **Fallback Modes**: Multiple strategies ensure compatibility
4. **Manual Installation**: Run `python install_deps.py` for platform-specific deps

The fix is applied automatically when the app starts.

#### Other Common Issues
- **API Key Error**: Ensure `GROQ_API_KEY` is set in your environment variables
- **File Upload Issues**: Check file permissions and ensure uploads directory exists
- **Memory Issues**: Consider upgrading your deployment plan for large PDF processing

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/resumatch_ai/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## 🔮 Future Enhancements

- [ ] Enhanced resume generation with complete rewriting
- [ ] Multiple LLM provider support
- [ ] Batch processing for multiple resumes
- [ ] Advanced ATS scoring system
- [ ] Resume template suggestions
- [ ] Industry-specific analysis

---

**Made with ❤️ using AI and open-source technologies**