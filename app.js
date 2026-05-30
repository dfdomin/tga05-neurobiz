const alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ".split("");
const bodyOrder = ["head", "torso", "left-arm", "right-arm", "left-leg", "right-leg"];

const state = {
  secret: "",
  normalizedSecret: "",
  guessed: new Set(),
  mistakes: 0,
  active: false,
  finished: false,
};

const elements = {
  form: document.querySelector("#secretForm"),
  input: document.querySelector("#secretInput"),
  start: document.querySelector("#startButton"),
  clear: document.querySelector("#clearButton"),
  reveal: document.querySelector("#revealButton"),
  newRound: document.querySelector("#newRoundButton"),
  toggleSecret: document.querySelector("#toggleSecretButton"),
  fullscreen: document.querySelector("#fullscreenButton"),
  keyboard: document.querySelector("#keyboard"),
  word: document.querySelector("#wordDisplay"),
  message: document.querySelector("#gameMessage"),
  used: document.querySelector("#usedLetters"),
  mistakes: document.querySelector("#mistakesCount"),
  maxMistakes: document.querySelector("#maxMistakes"),
  status: document.querySelector("#statusChip"),
  parts: document.querySelectorAll(".body-part"),
};

elements.maxMistakes.textContent = String(bodyOrder.length);

function normalizeText(value) {
  return value
    .toLocaleUpperCase("es-CO")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

function isGuessableCharacter(character) {
  return /[A-ZÑ]/.test(character);
}

function renderKeyboard() {
  elements.keyboard.innerHTML = "";
  alphabet.forEach((letter) => {
    const button = document.createElement("button");
    button.className = "key";
    button.type = "button";
    button.textContent = letter;
    button.dataset.letter = letter;
    button.disabled = !state.active || state.finished || state.guessed.has(letter);

    if (state.guessed.has(letter)) {
      button.classList.add(state.normalizedSecret.includes(letter) ? "correct" : "wrong");
    }

    button.addEventListener("click", () => guessLetter(letter));
    elements.keyboard.append(button);
  });
}

function renderWord(reveal = false) {
  elements.word.innerHTML = "";
  const source = state.secret || elements.input.value || "";
  const normalized = normalizeText(source);

  if (!source.trim()) {
    const empty = document.createElement("span");
    empty.className = "letter-slot";
    empty.textContent = "?";
    elements.word.append(empty);
    return;
  }

  Array.from(source).forEach((character, index) => {
    const normalizedCharacter = normalized[index] || character;
    const slot = document.createElement("span");
    slot.className = "letter-slot";

    if (character === " ") {
      slot.classList.add("space");
      slot.textContent = "";
    } else if (!isGuessableCharacter(normalizedCharacter)) {
      slot.textContent = character;
    } else if (reveal || state.guessed.has(normalizedCharacter)) {
      slot.textContent = character.toLocaleUpperCase("es-CO");
    } else {
      slot.textContent = "";
    }

    elements.word.append(slot);
  });
}

function renderDrawing() {
  elements.parts.forEach((part) => {
    const partName = part.dataset.part;
    const partIndex = bodyOrder.indexOf(partName);
    part.classList.toggle("lost", partIndex > -1 && partIndex < state.mistakes);
  });
}

function renderStatus() {
  elements.mistakes.textContent = String(state.mistakes);
  const guessedLetters = Array.from(state.guessed).sort((a, b) => a.localeCompare(b, "es"));
  elements.used.textContent = guessedLetters.length ? guessedLetters.join(" · ") : "Sin letras usadas";

  elements.status.classList.remove("danger", "win");
  if (!state.active) {
    elements.status.textContent = "Esperando palabra";
  } else if (state.finished && isWinner()) {
    elements.status.textContent = "Nombre descubierto";
    elements.status.classList.add("win");
  } else if (state.finished) {
    elements.status.textContent = "Ronda terminada";
    elements.status.classList.add("danger");
  } else {
    elements.status.textContent = "Adivinando";
  }
}

function renderAll(options = {}) {
  renderWord(options.reveal);
  renderDrawing();
  renderStatus();
  renderKeyboard();
}

function startGame() {
  const secret = elements.input.value.trim().replace(/\s+/g, " ");
  if (!secret) {
    elements.message.textContent = "Primero escribe un nombre o una palabra.";
    elements.input.focus();
    return;
  }

  state.secret = secret;
  state.normalizedSecret = normalizeText(secret);
  state.guessed = new Set();
  state.mistakes = 0;
  state.active = true;
  state.finished = false;
  elements.input.type = "password";
  elements.message.textContent = "Pide letras al grupo y toca cada intento.";
  renderAll();
}

function clearGame() {
  state.secret = "";
  state.normalizedSecret = "";
  state.guessed = new Set();
  state.mistakes = 0;
  state.active = false;
  state.finished = false;
  elements.input.value = "";
  elements.input.type = "password";
  elements.message.textContent = "Escribe una palabra o nombre y presiona Iniciar.";
  renderAll();
  elements.input.focus();
}

function newRound() {
  state.secret = "";
  state.normalizedSecret = "";
  state.guessed = new Set();
  state.mistakes = 0;
  state.active = false;
  state.finished = false;
  elements.input.value = "";
  elements.input.type = "password";
  elements.message.textContent = "Listo para otra persona o palabra.";
  renderAll();
  elements.input.focus();
}

function guessLetter(letter) {
  if (!state.active || state.finished || state.guessed.has(letter)) return;

  state.guessed.add(letter);
  if (!state.normalizedSecret.includes(letter)) {
    state.mistakes += 1;
  }

  if (isWinner()) {
    state.finished = true;
    elements.message.textContent = "¡Acertaron! La palabra quedó completa.";
  } else if (state.mistakes >= bodyOrder.length) {
    state.finished = true;
    elements.message.textContent = `Se acabaron los intentos. Era: ${state.secret}`;
  } else if (state.normalizedSecret.includes(letter)) {
    elements.message.textContent = `Bien: la letra ${letter} está en la palabra.`;
  } else {
    elements.message.textContent = `La letra ${letter} no está. Se tacha una parte del dibujo.`;
  }

  renderAll();
}

function isWinner() {
  if (!state.normalizedSecret) return false;
  return Array.from(state.normalizedSecret).every((character) => {
    return !isGuessableCharacter(character) || state.guessed.has(character);
  });
}

function toggleSecretVisibility() {
  elements.input.type = elements.input.type === "password" ? "text" : "password";
  elements.input.focus();
}

function revealSecret() {
  if (!state.secret) {
    elements.message.textContent = "No hay palabra activa para revelar.";
    return;
  }

  state.finished = true;
  elements.message.textContent = `La palabra era: ${state.secret}`;
  renderAll({ reveal: true });
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen?.();
  } else {
    document.exitFullscreen?.();
  }
}

elements.form.addEventListener("submit", (event) => {
  event.preventDefault();
  startGame();
});
elements.start.addEventListener("click", startGame);
elements.clear.addEventListener("click", clearGame);
elements.newRound.addEventListener("click", newRound);
elements.reveal.addEventListener("click", revealSecret);
elements.toggleSecret.addEventListener("click", toggleSecretVisibility);
elements.fullscreen.addEventListener("click", toggleFullscreen);
elements.input.addEventListener("input", () => {
  if (!state.active) renderWord();
});

renderAll();
