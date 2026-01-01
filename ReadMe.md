# Python Mini Assignments (Career Taste Test)

Goal: give you a quick, practical feel for what programming work looks like, without drowning in theory.

You will do these assignments in order:
1. Hello World
2. Strings
3. Arguments (command line)
4. Files (read and write)
5. GDP (tiny data analytics project)

Each assignment lives in its own folder and has:
- `README.md` with the task
- `main.py` to implement

---

## Big picture: who builds what

### Frontend developer
Builds what users see and click.
- Websites and web apps
- Mostly HTML, CSS, JavaScript/TypeScript
- Think: buttons, pages, forms, UI logic

### Backend developer
Builds the logic behind the scenes.
- APIs, databases, authentication, business rules
- Often Python, Java, C#, Go, Node.js
- Think: “When you click Pay, what happens on the server?”

### DevOps / Platform engineer
Makes software reliably run in real life.
- Deployments, monitoring, CI/CD pipelines, infrastructure
- Think: “How do we ship changes safely and keep systems stable?”

### Cloud engineer
Builds and operates things on AWS/Azure/GCP.
- Networking, compute, storage, security, automation
- Think: “How do we run this in the cloud with good security and cost control?”

### Data scientist / data analyst
Uses data to answer questions and support decisions.
- Cleaning data, analysis, visualization, simple models
- Often Python and SQL
- Think: “What is happening, why, and what might happen next?”

### Data engineer
Builds data pipelines and data platforms.
- Ingesting data, transforming it, making it reliable
- Think: “How do we get trustworthy data to the right place every day?”

---

## Terminal, interpreter, and running code

### What is the terminal?
The terminal is a text-based way to run commands on your computer.
On Windows you can use:
- PowerShell (recommended)
- Command Prompt

Open Powershell and try these commands 
type them and push enter:
```bash
dir
cd ..
mkdir test_folder
rmdir test_folder
```
### What is an interpreter?
Python is an interpreted language.
That means:
- You write Python code in a `.py` file
- The Python interpreter reads and runs it

### Getting Python on your computer
Open a (normal) terminal aka Powershell or a warp terminal (agentic terminal)

before warp you could do something like this (if you have winget installed)

```bash
winget install Python.Python.3.12
```
This will:

- Download Python from the official source
- Install it system-wide
- Automatically add Python to PATH  (windows pc's need to have programs added to the path otherwis it can't find it)

then run the following commands to check if the installation was successfull 

```bash
python --version
python main.py
```


But now we have warp so you can just ask warp to install python version 3.12 and add it to your path, or you can go to the website and do it in the noob way


### Virtual environments (short and honest)

A virtual environment is an isolated Python setup for one project.
Why they exist:
- Different projects need different versions of libraries
- Without isolation, things break fast

Example problem:
- Project A needs pandas 1.x
- Project B needs pandas 2.x

One global Python cannot satisfy both safely
Virtual environments solve this.

Why you do NOT need one yet
These exercises:
- Use only Python’s standard library
- Do not install external packages
- Will run on any clean Python install

So we intentionally skip virtual environments for now.
You will need them later when:
- Installing libraries like numpy, pandas, requests, fastapi
- Working on real projects or in a team
- When that moment comes, we will add them. or warp will