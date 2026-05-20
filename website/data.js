// Shared data for all aesthetic variations.
// Pulled from github.com/Mrinank-Bhowmick/python-beginner-projects

window.PBP_PROJECTS = [
  { id: 'snake', name: 'Snake Game', cat: 'games', blurb: 'Slither, eat, grow longer. The classic.', lines: 92, deps: 'pygame', emoji: '🐍' },
  { id: 'tictactoe', name: 'Tic-Tac-Toe', cat: 'games', blurb: 'Three in a row, terminal showdown.', lines: 64, deps: 'stdlib', emoji: '⭕', runnable: true },
  { id: 'hangman', name: 'Hangman', cat: 'games', blurb: 'Guess letters before the gallows complete.', lines: 78, deps: 'stdlib', emoji: '🪢', runnable: true },
  { id: 'flappy', name: 'Flappy Bird', cat: 'games', blurb: 'Tap to flap. Avoid the pipes. Die. Repeat.', lines: 140, deps: 'pygame', emoji: '🐦' },
  { id: 'rps', name: 'Rock · Paper · Scissors', cat: 'games', blurb: 'Best of three vs the random module.', lines: 48, deps: 'stdlib', emoji: '✊', runnable: true },
  { id: 'calc', name: 'Calculator', cat: 'tools', blurb: 'Tkinter buttons. Operator precedence. Beep.', lines: 110, deps: 'tkinter', emoji: '🧮' },
  { id: 'bmi', name: 'BMI Calculator', cat: 'tools', blurb: 'Height + weight → a single questionable number.', lines: 36, deps: 'stdlib', emoji: '⚖️', runnable: true },
  { id: 'weather', name: 'Weather App', cat: 'web', blurb: 'OpenWeather API, your city, today.', lines: 88, deps: 'requests', emoji: '☁️' },
  { id: 'qr', name: 'QR Code Generator', cat: 'tools', blurb: 'Text in, scannable square out.', lines: 22, deps: 'qrcode', emoji: '▦', runnable: true },
  { id: 'pwd', name: 'Password Generator', cat: 'tools', blurb: 'Random, strong, immediately forgotten.', lines: 30, deps: 'secrets', emoji: '🔐' },
  { id: 'yt', name: 'YouTube Downloader', cat: 'web', blurb: 'pytube wrapper. Save the lecture.', lines: 54, deps: 'pytube', emoji: '⬇' },
  { id: 'madlibs', name: 'Madlibs Generator', cat: 'fun', blurb: 'Fill in nouns. Receive nonsense. Laugh.', lines: 40, deps: 'stdlib', emoji: '✏️', runnable: true },
];

window.PBP_CATEGORIES = [
  { id: 'all', name: 'All', count: 12 },
  { id: 'games', name: 'Games', count: 5 },
  { id: 'tools', name: 'Tools', count: 4 },
  { id: 'web', name: 'Web & API', count: 2 },
  { id: 'fun', name: 'Just for Fun', count: 1 },
];

window.PBP_CONTRIBUTORS = [
  { handle: 'Mrinank-Bhowmick', name: 'Mrinank Bhowmick', commits: 412, role: 'maintainer' },
  { handle: 'ibra-kdbra', name: 'Ibra-kdbra', commits: 38 },
  { handle: 'PythonicBoat', name: 'Yashvardhan Singh', commits: 27 },
  { handle: 'Alby084', name: 'Alby084', commits: 24 },
  { handle: 'ca20110820', name: 'Cedric Anover', commits: 21 },
  { handle: 'kanchanraiii', name: 'Kanchan Rai', commits: 18 },
  { handle: 'TERNION-1121', name: 'Vikrant Bhadouriya', commits: 16 },
  { handle: 'Guyunjeong', name: 'Chloe', commits: 14 },
  { handle: 'rik-chatterjee', name: 'Rik Chatterjee', commits: 12 },
  { handle: 'omkarxpatel', name: 'Omkar Patel', commits: 11 },
  { handle: 'UffaModey', name: 'Fafa Modey', commits: 10 },
  { handle: 'anish2105', name: 'Anish Vantagodi', commits: 9 },
  { handle: 'JohnRTitor', name: 'Masum Reza', commits: 9 },
  { handle: 'sudipg4112001', name: 'Sudip Ghosh', commits: 8 },
  { handle: 'shashaaankkkkk', name: 'Shashank Shekhar', commits: 8 },
  { handle: 'jrbublitz', name: 'Jefferson Bublitz', commits: 7 },
  { handle: 'vagxrth', name: 'Vagarth Pandey', commits: 7 },
  { handle: 'shriyansnaik', name: 'Shriyans Naik', commits: 6 },
  { handle: 'xlo-u', name: 'Yash Upadhyay', commits: 6 },
  { handle: 'payallenka', name: 'Payallenka', commits: 5 },
];

window.PBP_STATS = { projects: 100, contributors: 241, stars: 2300, forks: 903 };

window.PBP_PATHS = [
  { id: 'starter', name: 'First Steps', tag: 'Day 1', desc: 'Variables, input, print. Calculator → BMI → RPS.', items: ['bmi', 'rps', 'calc'], hue: 0 },
  { id: 'games',   name: 'Make Games',  tag: 'Week 1', desc: 'Loops, state, the random module. Tic-Tac-Toe → Hangman → Snake.', items: ['tictactoe', 'hangman', 'snake'], hue: 1 },
  { id: 'real',    name: 'Real World',  tag: 'Week 2', desc: 'HTTP, files, libraries. Weather → QR → YouTube.', items: ['weather', 'qr', 'yt'], hue: 2 },
];

// Shared bookmark helper (localStorage)
window.PBP_BM = {
  KEY: 'pbp_bookmarks_v1',
  get() { try { return JSON.parse(localStorage.getItem(this.KEY)) || []; } catch { return []; } },
  set(arr) { localStorage.setItem(this.KEY, JSON.stringify(arr)); },
  toggle(id) {
    const arr = this.get();
    const i = arr.indexOf(id);
    if (i >= 0) arr.splice(i, 1); else arr.push(id);
    this.set(arr);
    return arr;
  },
};
