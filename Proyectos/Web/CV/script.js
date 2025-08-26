// Cyberpunk CV Website - JavaScript Functionality

// Wait for DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  initializeWebsite();
});

// Main initialization function
function initializeWebsite() {
  initializeMatrixRain();
  initializeTerminal();
  initializeNavigation();
  initializeSkills();
  initializeTimeline();
  initializeAvatar();
  initializeGlitchEffects();
  updateTime();

  // Update time every second
  setInterval(updateTime, 1000);
}

// Matrix Rain Effect
function initializeMatrixRain() {
  const canvas = document.getElementById("matrix-canvas");
  const ctx = canvas.getContext("2d");

  // Resize canvas to full screen
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  resizeCanvas();
  window.addEventListener("resize", resizeCanvas);

  const matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%+-/~{[|`]}";
  const matrixArray = matrix.split("");

  const fontSize = 14;
  const columns = canvas.width / fontSize;
  const drops = [];

  // Initialize drops
  for (let x = 0; x < columns; x++) {
    drops[x] = 1;
  }

  function draw() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.04)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#00ff00";
    ctx.font = `${fontSize}px JetBrains Mono, monospace`;

    for (let i = 0; i < drops.length; i++) {
      if (Math.random() > 0.5) {
        // Reduced density
        const text =
          matrixArray[Math.floor(Math.random() * matrixArray.length)];
        ctx.fillStyle = i % 2 === 0 ? "#00ff00" : "#00cc00";
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
          drops[i] = 0;
        }

        drops[i] += 0.5; // Slower speed
      }
    }

    requestAnimationFrame(draw);
  }

  draw();
}

// Terminal Functionality
function initializeTerminal() {
  const terminalInput = document.getElementById("terminal-input");
  const terminalContent = document.getElementById("terminal-content");

  let commandHistory = [];
  let historyIndex = -1;
  let isTyping = false;

  const username = "h4ckxel";
  const hostname = "fsociety";
  const currentPath = "~/portfolio";

  // Terminal commands
  const commands = {
    help: {
      description: "Show available commands",
      execute: () => [
        "Available commands:",
        "  help          - Show this help message",
        "  about         - Display information about me",
        "  skills        - List technical skills",
        "  experience    - Show work experience",
        "  projects      - Display portfolio projects",
        "  contact       - Show contact information",
        "  clear         - Clear terminal screen",
        "  whoami        - Display current user",
        "  pwd           - Print working directory",
        "  ls            - List directory contents",
        "  cat [file]    - Display file contents",
        "  neofetch      - Show system information",
        "  matrix        - Enter the matrix...",
        "",
        "Use TAB for autocompletion, UP/DOWN arrows for command history",
      ],
    },

    about: {
      description: "Display information about me",
      execute: () => [
        "╔══════════════════════════════════════════════════════════════╗",
        "║                          ABOUT ME                            ║",
        "╠══════════════════════════════════════════════════════════════╣",
        "║ Name: Acxel Tesfaye                                          ║",
        "║ Role: Software Engineering Student | Ethical Hacking Learner ║",
        "║ Location: Mexico / The Digital Frontier                      ║",
        "║                                                              ║",
        "║ Soy estudiante de Ingeniería en Software con interés en la   ║",
        "║ ciberseguridad y el hacking ético. Actualmente me encuentro  ║",
        "║ en la etapa de formación, aprendiendo y aplicando conceptos  ║",
        "║ fundamentales de programación, redes y sistemas operativos.  ║",
        "║                                                              ║",
        "║ Me motiva entender cómo funcionan las tecnologías a nivel    ║",
        "║ profundo, explorando desde el desarrollo hasta la seguridad, ║",
        "║ con el objetivo de construir soluciones y fortalecer sistemas║",
        "║ frente a vulnerabilidades.                                   ║",
        "║                                                              ║",
        "║ En mi tiempo libre practico en entornos Linux, laboratorios  ║",
        "║ de pentesting y retos de programación, siempre con la visión ║",
        "║ de crecer en el ámbito del software y la seguridad informáti-║",
        "║ ca.                                                          ║",
        "╚══════════════════════════════════════════════════════════════╝",

      ],
    },

    skills: {
      description: "List technical skills",
      execute: () => [
        "TECHNICAL SKILLS MATRIX:",
        "",
        "💻 Programming Languages:",
        "   ▸ C/C++  [██████████ ] Intermediate",
        "   ▸ Python [█████████  ] Intermediate",
        "",
        "🔒 Security:",
        "   ▸ Penetration Testing    [█████████   ] Advanced - Learning",
      ],
    },

    experience: {
  description: "Show work experience",
  execute: () => [
    "WORK EXPERIENCE TIMELINE:",
    "",
    "┌─ University Projects:",
    "│  ▸ Desarrollo de programas en C/C++, Python y Java",
    "│    aplicados a lógica, algoritmos y estructuras de datos",
    "│  ▸ Implementación de pequeños sistemas y utilidades",
    "│    como parte de proyectos académicos",
    "│",
    "├─ Personal Projects & Labs (2023-Present)",
    "│  ▸ Configuración y personalización de entornos Linux",
    "│    usando Bash y Lua",
    "│  ▸ Desarrollo de scripts en Python para automatización",
    "│    y resolución de problemas de seguridad",
    "│  ▸ Laboratorios de pentesting con Kali Linux",
    "│    (escaneo, enumeración, explotación básica)",
    "│",
    "├─ Cybersecurity Training & Challenges:",
    "│  ▸ Participación en CTFs y wargames (OverTheWire, TryHackMe)",
    "│  ▸ Prácticas de análisis de vulnerabilidades y uso de",
    "│    herramientas como Nmap, Metasploit, Burp Suite",
    "│  ▸ Estudio autodidacta en fundamentos de redes,",
    "│    criptografía y hardening de sistemas",
    "│",
    "└─ Open Source & Learning Contributions:",
    "   ▸ Aportes en configuraciones, dotfiles y scripts para",
    "     entornos Unix-like",
    "   ▸ Exploración de técnicas de ingeniería inversa básica",
    "   ▸ Documentación y experimentación con exploits en entornos",
    "     controlados de laboratorio",
  ],
},


    projects: {
  description: "Display portfolio projects",
  execute: () => [
    "PORTFOLIO PROJECTS:",
    "",
    "• GitHub: h4ckxel — Ethical Hacking & Security Tools",
    "   • CVE-2025-2005 (Exploit PoC)",
    "     – Exploración de una vulnerabilidad crítica de carga arbitraria en plugin WordPress;",
    "       exploit en Python (PoC) para demostrar ejecución remota. https://github.com/h4ckxel/CVE-2025-2005",
    "   • cheat-sheet-Python",
    "     – Hoja de referencia en Python con ejemplos desde básicos a POO (Programación Orientada a Objetos). :contentReference[oaicite:1]{index=1}",
    "",
    "• ResearchGate Publications — Matemáticas & Criptografía",
    "   • “Espiral de Ulam y Patrones de los Números Primos: Un Análisis Matemático y Visual”",
    "     – Estudio de la disposición gráfica de números que revela patrones en la distribución de números primos,",
    "       con conexiones a teoría de números y criptografía. Publicado en septiembre de 2024. :contentReference[oaicite:2]{index=2}",
    "   • “Implementación de la Criba de Eratóstenes en Bash y sus Aplicaciones”",
    "     – Scripts en Bash para calcular números primos eficientemente, aplicables en contextos criptográficos y de seguridad.",
    "       Publicado en septiembre de 2024. :contentReference[oaicite:3]{index=3}",
    "",
    "• Community & Open Source Engagement",
    "   • Participación activa en discusiones de GitHub Community,",
    "     compartiendo consejos para comenzar en open source y ética hacker. :contentReference[oaicite:4]{index=4}",
    "",
    "PORTFOLIO SUMMARY:",
    "- Combino conocimientos de ciberseguridad, scripting y teoría matemática.",
    "- Mi enfoque cruza hacking ético, automatización, visualización matemática y software libre.",
    "- Todos los proyectos están disponibles en GitHub y ResearchGate para revisión.",
  ],
},


    contact: {
      description: "Show contact information",
      execute: () => [
        "📡 CONTACT MATRIX:",
        "",
        "┌────────────────────────────────────────────────────────┐",
        "│                    SECURE CHANNELS                     │",
        "├────────────────────────────────────────────────────────┤",
        "│ 📧 Email:     h4ckxel@gmail.com                        │",
        "│ 🐙 GitHub:    github.com/h4ckxel                       │",
        "│ 💼 LinkedIn:  linkedin.com/in/cyber-developer          │",
        "│ 🐦 X:         @h4ckxel                                 │",
        "│ 💬 Discord:   h4ckxel#1337                             │",
        "└────────────────────────────────────────────────────────┘",
        "",
        "🔐 PGP Key Fingerprint: 4A1E 2C3D 4C5F 6789 ABCD EF01 2845 6789",
        "",
        "⚠️  All communications are end-to-end encrypted ⚠️",
      ],
    },

    clear: {
      description: "Clear terminal screen",
      execute: () => [],
    },

    whoami: {
      description: "Display current user",
      execute: () => [username],
    },

    pwd: {
      description: "Print working directory",
      execute: () => [`/home/${username}/portfolio`],
    },

    ls: {
      description: "List directory contents",
      execute: () => [
        "total 42",
        "drwxr-xr-x  8 hacker hacker  4096 Dec 13 23:59 .",
        "drwxr-xr-x  3 hacker hacker  4096 Dec 13 20:00 ..",
        "-rw-r--r--  1 hacker hacker   220 Dec 13 20:00 .bash_logout",
        "-rw-r--r--  1 hacker hacker  3771 Dec 13 20:00 .bashrc",
        "drwx------  2 hacker hacker  4096 Dec 13 20:01 .cache",
        "-rw-r--r--  1 hacker hacker   807 Dec 13 20:00 .profile",
        "drwxr-xr-x  2 hacker hacker  4096 Dec 13 23:59 projects",
        "-rw-r--r--  1 hacker hacker  2048 Dec 13 23:58 README.md",
        "-rw-r--r--  1 hacker hacker  1024 Dec 13 23:57 skills.txt",
        "drwxr-xr-x  2 hacker hacker  4096 Dec 13 23:56 experience",
      ],
    },

    neofetch: {
      description: "Show system information",
      execute: () => [
        "                   .88888888:.",
        "                  88888888.88888.",
        "                .8888888888888888.",
        "                888888888888888888",
        "                88' _`88'_  `88888",
        "                88 88 88 88  88888",
        "                88_88_::_88_:88888",
        "                88:::,::,:::::8888",
        "                88`::::::::::':`88",
        "               .88`:::::::::::::`,88",
        "              .8888:::::::::::::::88",
        "             .8888':::::::::::::::88",
        "            .8888':::::::::::::::::88",
        "           .8888:::::::::::::::::::88",
        "          .8888:::::::::::::::::::'88",
        "         .8888:::::::::::::::::::'  88",
        "        .8888:::::::::::::::::::'  .88",
        "       .8888:::::::::::::::::::'  .888",
        "",
        `${username}@${hostname}`,
        "─".repeat(30),
        "OS: CyberLinux x86_64",
        "Host: Quantum Computer Pro",
        "Kernel: 6.9.0-cyber",
        "Uptime: 13 days, 37 hours, 42 mins",
        "Packages: 2048 (apt), 512 (snap)",
        "Shell: zsh 5.9",
        "Resolution: 3840x2160",
        "DE: Cyber Desktop Environment",
        "WM: i3-gaps",
        "Theme: CyberPunk-Neon",
        "Terminal: cyber-terminal",
        "CPU: Intel Core i9-13900K (24) @ 5.8GHz",
        "GPU: NVIDIA RTX 4090 TI",
        "Memory: 8192MiB / 32768MiB",
      ],
    },

    matrix: {
      description: "Enter the matrix...",
      execute: () => [
        "Entering the Matrix...",
        "",
        "01001000 01100001 01100011 01101011 01100101 01110010",
        "01001101 01100001 01110100 01110010 01101001 01111000",
        "",
        "⠊⠉⠑⠀⠞⠕⠀⠍⠑⠑⠞⠀⠽⠕⠥⠂⠀⠝⠑⠕⠲⠲⠲",
        "",
        "The Matrix has you...",
        "Follow the white rabbit 🐰",
        "",
        "Wake up, Neo...",
        "The Matrix is calling you.",
        "",
        "> red_pill.exe executed successfully",
        "> Connecting to Zion mainframe...",
        "> Welcome to the real world.",
      ],
    },
  };

  // Add line to terminal
  function addLine(type, content) {
    const line = document.createElement("div");
    line.className = `terminal-line ${type}`;
    line.textContent = content;
    terminalContent.appendChild(line);
    terminalContent.scrollTop = terminalContent.scrollHeight;
  }

  // Execute command
  async function executeCommand(cmd) {
    const trimmedCmd = cmd.trim();

    if (!trimmedCmd) return;

    // Add command to history
    commandHistory.push(trimmedCmd);
    historyIndex = -1;

    // Add command line
    addLine("command", `${username}@${hostname}:${currentPath}$ ${trimmedCmd}`);

    // Handle special commands
    if (trimmedCmd === "clear") {
      terminalContent.innerHTML = "";
      return;
    }

    // Parse command and arguments
    const [baseCmd, ...args] = trimmedCmd.split(" ");

    if (commands[baseCmd]) {
      isTyping = true;

      // Simulate typing delay
      await new Promise((resolve) =>
        setTimeout(resolve, 300 + Math.random() * 700),
      );

      const output = commands[baseCmd].execute();
      output.forEach((line) => {
        addLine("output", line);
      });

      isTyping = false;
    } else if (baseCmd === "cat" && args.length > 0) {
      // Handle cat command with file arguments
      const filename = args[0];
      isTyping = true;
      await new Promise((resolve) => setTimeout(resolve, 200));

      if (filename === "README.md") {
        addLine("output", "# Welcome to My Digital Portfolio");
        addLine("output", "");
        addLine(
          "output",
          "This is the personal portfolio of a cybersecurity expert",
        );
        addLine(
          "output",
          "and full-stack developer living in the digital frontier.",
        );
        addLine("output", "");
        addLine("output", "Type `help` to see available commands.");
      } else if (filename === "skills.txt") {
        addLine(
          "output",
          "JavaScript, TypeScript, React, Node.js, Python, Go, Rust",
        );
        addLine("output", "Docker, Kubernetes, AWS, GCP, PostgreSQL, MongoDB");
        addLine("output", "Penetration Testing, Security Analysis, DevOps");
      } else {
        addLine("error", `cat: ${filename}: No such file or directory`);
      }

      isTyping = false;
    } else {
      addLine(
        "error",
        `Command '${baseCmd}' not found. Type 'help' for available commands.`,
      );
    }
  }

  // Handle keyboard input
  terminalInput.addEventListener("keydown", function (e) {
    if (isTyping) {
      e.preventDefault();
      return;
    }

    if (e.key === "Enter") {
      executeCommand(terminalInput.value);
      terminalInput.value = "";
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      if (commandHistory.length > 0) {
        const newIndex =
          historyIndex === -1
            ? commandHistory.length - 1
            : Math.max(0, historyIndex - 1);
        historyIndex = newIndex;
        terminalInput.value = commandHistory[newIndex] || "";
      }
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      if (historyIndex !== -1) {
        const newIndex = historyIndex + 1;
        if (newIndex >= commandHistory.length) {
          historyIndex = -1;
          terminalInput.value = "";
        } else {
          historyIndex = newIndex;
          terminalInput.value = commandHistory[newIndex];
        }
      }
    } else if (e.key === "Tab") {
      e.preventDefault();
      const availableCommands = Object.keys(commands).filter((cmd) =>
        cmd.startsWith(terminalInput.value.toLowerCase()),
      );
      if (availableCommands.length === 1) {
        terminalInput.value = availableCommands[0];
      } else if (availableCommands.length > 1) {
        addLine("info", `Available: ${availableCommands.join(", ")}`);
      }
    }
  });

  // Focus terminal input when clicking anywhere on terminal
  document.addEventListener("click", function () {
    terminalInput.focus();
  });

  // Initial focus
  terminalInput.focus();
}

// Navigation functionality
function initializeNavigation() {
  const navButtons = document.querySelectorAll(".nav-btn");
  const floatingNavDots = document.querySelectorAll(".nav-dot");
  const contentSections = document.querySelectorAll(".content-section");

  function showSection(sectionId) {
    // Hide all sections
    contentSections.forEach((section) => {
      section.classList.remove("active");
    });

    // Show target section
    const targetSection = document.getElementById(`${sectionId}-section`);
    if (targetSection) {
      targetSection.classList.add("active");
    }

    // Update nav button states
    navButtons.forEach((btn) => {
      btn.classList.remove("active");
      if (btn.dataset.section === sectionId) {
        btn.classList.add("active");
      }
    });

    // Update floating nav dots
    floatingNavDots.forEach((dot) => {
      dot.classList.remove("active");
      if (dot.dataset.section === sectionId) {
        dot.classList.add("active");
      }
    });
  }

  // Add click handlers
  navButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      showSection(btn.dataset.section);
    });
  });

  floatingNavDots.forEach((dot) => {
    dot.addEventListener("click", () => {
      showSection(dot.dataset.section);
    });
  });
}

// Skills functionality
function initializeSkills() {
  const skillsData = [
    // Frontend
    {
      name: "React",
      level: 95,
      category: "frontend",
      icon: "⚛️",
      description: "Advanced component architecture & hooks",
    },
    {
      name: "TypeScript",
      level: 90,
      category: "frontend",
      icon: "🔷",
      description: "Type-safe development & advanced patterns",
    },
    {
      name: "Next.js",
      level: 88,
      category: "frontend",
      icon: "▲",
      description: "SSR, SSG, and App Router mastery",
    },
    {
      name: "Tailwind CSS",
      level: 92,
      category: "frontend",
      icon: "🎨",
      description: "Utility-first design systems",
    },
    {
      name: "Three.js",
      level: 75,
      category: "frontend",
      icon: "🎮",
      description: "3D graphics and WebGL",
    },

    // Backend
    {
      name: "Node.js",
      level: 93,
      category: "backend",
      icon: "🟢",
      description: "Scalable server-side applications",
    },
    {
      name: "Python",
      level: 87,
      category: "backend",
      icon: "🐍",
      description: "Django, FastAPI, and data science",
    },
    {
      name: "Go",
      level: 78,
      category: "backend",
      icon: "🐹",
      description: "High-performance microservices",
    },
    {
      name: "PostgreSQL",
      level: 85,
      category: "backend",
      icon: "🐘",
      description: "Complex queries and optimization",
    },
    {
      name: "GraphQL",
      level: 82,
      category: "backend",
      icon: "📊",
      description: "Apollo Server and schema design",
    },

    // DevOps
    {
      name: "Docker",
      level: 88,
      category: "devops",
      icon: "🐳",
      description: "Containerization and multi-stage builds",
    },
    {
      name: "Kubernetes",
      level: 80,
      category: "devops",
      icon: "☸️",
      description: "Orchestration and service mesh",
    },
    {
      name: "AWS",
      level: 85,
      category: "devops",
      icon: "☁️",
      description: "Lambda, ECS, RDS, and more",
    },
    {
      name: "Terraform",
      level: 75,
      category: "devops",
      icon: "🏗️",
      description: "Infrastructure as Code",
    },

    // Security
    {
      name: "Penetration Testing",
      level: 82,
      category: "security",
      icon: "🔓",
      description: "OWASP methodologies",
    },
    {
      name: "Cryptography",
      level: 78,
      category: "security",
      icon: "🔐",
      description: "PKI and secure communications",
    },

    // Other
    {
      name: "Machine Learning",
      level: 72,
      category: "other",
      icon: "🤖",
      description: "TensorFlow and PyTorch",
    },
    {
      name: "Blockchain",
      level: 68,
      category: "other",
      icon: "⛓️",
      description: "Smart contracts and Web3",
    },
  ];

  const skillsGrid = document.getElementById("skills-grid");
  const filterButtons = document.querySelectorAll(".filter-btn");

  function getLevelClass(level) {
    if (level >= 90) return "expert";
    if (level >= 80) return "advanced";
    if (level >= 70) return "intermediate";
    return "learning";
  }

  function createSkillCard(skill, index) {
    return `
      <div class="skill-card ${skill.category}" style="animation-delay: ${index * 50}ms">
        <div class="skill-header">
          <div class="skill-name-row">
            <span class="skill-icon">${skill.icon}</span>
            <h3 class="skill-name">${skill.name}</h3>
          </div>
          <span class="skill-level ${skill.category}">${skill.level}%</span>
        </div>
        <div class="skill-progress">
          <div class="skill-progress-bar ${skill.category}" style="width: ${skill.level}%"></div>
        </div>
        <p class="skill-description">${skill.description}</p>
        <div class="skill-level-indicator ${getLevelClass(skill.level)}"></div>
      </div>
    `;
  }

  function renderSkills(category = "all") {
    const filteredSkills =
      category === "all"
        ? skillsData
        : skillsData.filter((skill) => skill.category === category);
    skillsGrid.innerHTML = filteredSkills.map(createSkillCard).join("");

    // Animate progress bars
    setTimeout(() => {
      const progressBars = skillsGrid.querySelectorAll(".skill-progress-bar");
      progressBars.forEach((bar) => {
        bar.style.width = bar.style.width;
      });
    }, 100);
  }

  // Filter functionality
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterButtons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderSkills(btn.dataset.category);
    });
  });

  // Initial render
  renderSkills();
}

// Timeline functionality
function initializeTimeline() {
  const timelineData = [
    {
      id: "1",
      title: "Senior Full-Stack Engineer",
      company: "CyberCorp Industries",
      period: "2022 - Present",
      description: [
        "Lead development of mission-critical applications serving 10M+ users",
        "Architected microservices infrastructure with 99.9% uptime",
        "Implemented zero-downtime deployment strategies using K8s",
        "Mentored team of 8 developers and established code review processes",
      ],
      technologies: ["React", "Node.js", "Kubernetes", "AWS", "PostgreSQL"],
      type: "work",
      status: "current",
    },
    {
      id: "2",
      title: "Software Engineer",
      company: "Digital Nexus Labs",
      period: "2020 - 2022",
      description: [
        "Built scalable web applications using React and Node.js",
        "Developed RESTful APIs and GraphQL services",
        "Optimized database performance reducing query time by 60%",
        "Collaborated with cross-functional teams in agile environment",
      ],
      technologies: ["React", "Node.js", "GraphQL", "MongoDB", "Docker"],
      type: "work",
      status: "completed",
    },
    {
      id: "3",
      title: "Junior Developer",
      company: "StartupTech Solutions",
      period: "2019 - 2020",
      description: [
        "Contributed to frontend development using modern frameworks",
        "Participated in code reviews and testing processes",
        "Learned best practices for software development lifecycle",
        "Gained experience with version control and deployment pipelines",
      ],
      technologies: ["JavaScript", "Vue.js", "Python", "Git", "Jenkins"],
      type: "work",
      status: "completed",
    },
    {
      id: "4",
      title: "Computer Science Degree",
      company: "Cyber University",
      period: "2015 - 2019",
      description: [
        "Graduated Summa Cum Laude with 3.9 GPA",
        "Specialized in Cybersecurity and Machine Learning",
        "Led university hackathon team to 3 consecutive victories",
        "Published research on neural network optimization",
      ],
      technologies: ["Python", "C++", "Machine Learning", "Cryptography"],
      type: "education",
      status: "completed",
    },
  ];

  const timeline = document.getElementById("timeline");

  function getTypeIcon(type) {
    switch (type) {
      case "work":
        return "💼";
      case "education":
        return "🎓";
      case "project":
        return "🚀";
      default:
        return "📍";
    }
  }

  function createTimelineItem(item, index) {
    const currentBadge =
      item.status === "current"
        ? '<div class="current-badge">CURRENT</div>'
        : "";
    const currentClass = item.status === "current" ? "current" : "";

    return `
      <div class="timeline-item ${currentClass}" style="animation-delay: ${index * 200}ms">
        <div class="timeline-node">${getTypeIcon(item.type)}</div>
        <div class="timeline-content">
          ${currentBadge}
          <div class="timeline-header">
            <div>
              <h3 class="timeline-title glitch-text" data-text="${item.title}">${item.title}</h3>
              <p class="timeline-company">${item.company}</p>
            </div>
            <div class="timeline-period">${item.period}</div>
          </div>
          <ul class="timeline-description">
            ${item.description.map((desc) => `<li>${desc}</li>`).join("")}
          </ul>
          <div class="timeline-technologies">
            ${item.technologies.map((tech) => `<span class="tech-chip">${tech}</span>`).join("")}
          </div>
        </div>
      </div>
    `;
  }

  // Render timeline
  timeline.innerHTML = timelineData.map(createTimelineItem).join("");

  // Add end marker
  timeline.innerHTML += `
    <div class="timeline-item" style="animation-delay: ${timelineData.length * 200}ms">
      <div class="timeline-node" style="background: var(--neon-accent); border-color: var(--neon-accent);">✨</div>
      <div class="timeline-content">
        <h3 class="timeline-title glitch-text" data-text="The journey continues...">The journey continues...</h3>
      </div>
    </div>
  `;
}

// Avatar functionality
function initializeAvatar() {
  const avatarContainer = document.querySelector(".avatar-container");
  const holoInfo = document.querySelector(".holo-info");

  if (avatarContainer && holoInfo) {
    avatarContainer.addEventListener("mouseenter", () => {
      holoInfo.classList.remove("hidden");
    });

    avatarContainer.addEventListener("mouseleave", () => {
      holoInfo.classList.add("hidden");
    });
  }
}

// Glitch effects
function initializeGlitchEffects() {
  const glitchElements = document.querySelectorAll(".glitch-text");

  glitchElements.forEach((element) => {
    // Set data-text attribute if not present
    if (!element.hasAttribute("data-text")) {
      element.setAttribute("data-text", element.textContent);
    }

    // Random glitch effect
    if (element.dataset.trigger !== "hover") {
      setInterval(
        () => {
          if (Math.random() > 0.7) {
            element.style.animation = "glitch 0.3s";
            setTimeout(() => {
              element.style.animation = "";
            }, 300);
          }
        },
        3000 + Math.random() * 2000,
      );
    }
  });
}

// Update time display
function updateTime() {
  const timeElement = document.querySelector(".terminal-time");
  if (timeElement) {
    timeElement.textContent = new Date().toLocaleTimeString();
  }
}

// Intersection Observer for animations
function initializeIntersectionObserver() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate");
      }
    });
  }, observerOptions);

  // Observe elements for animation
  const animatedElements = document.querySelectorAll(
    ".skill-card, .timeline-item, .contact-method",
  );
  animatedElements.forEach((el) => observer.observe(el));
}

// Handle mobile touch interactions
function initializeMobileInteractions() {
  // Disable hover effects on touch devices
  if ("ontouchstart" in window) {
    document.body.classList.add("touch-device");
  }

  // Handle mobile navigation
  const navButtons = document.querySelectorAll(".nav-btn");
  navButtons.forEach((btn) => {
    btn.addEventListener("touchstart", function () {
      this.classList.add("touch-active");
    });

    btn.addEventListener("touchend", function () {
      this.classList.remove("touch-active");
    });
  });
}

// Performance optimizations
function initializePerformanceOptimizations() {
  // Throttle scroll events
  let ticking = false;

  function updateScrollEffects() {
    // Add any scroll-based effects here
    ticking = false;
  }

  function requestTick() {
    if (!ticking) {
      requestAnimationFrame(updateScrollEffects);
      ticking = true;
    }
  }

  window.addEventListener("scroll", requestTick);

  // Optimize animations for mobile
  if (window.innerWidth <= 768) {
    const style = document.createElement("style");
    style.textContent = `
      .animate-pulse-neon { animation-duration: 4s !important; }
      .animate-glitch { animation-duration: 0.5s !important; }
    `;
    document.head.appendChild(style);
  }
}

// Error handling
window.addEventListener("error", function (e) {
  console.error("JavaScript error:", e.error);
});

// Initialize additional features when DOM is ready
document.addEventListener("DOMContentLoaded", function () {
  initializeIntersectionObserver();
  initializeMobileInteractions();
  initializePerformanceOptimizations();
});

// Service Worker registration (optional)
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    // Uncomment if you want to add offline functionality
    // navigator.serviceWorker.register('/sw.js');
  });
}
