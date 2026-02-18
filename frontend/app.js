const profileForm = document.getElementById('profileForm');
const profileSetup = document.getElementById('profile-setup');
const matchCard = document.getElementById('match-card');

const matchName = document.getElementById('match-name');
const matchRole = document.getElementById('match-role');
const matchTags = document.getElementById('match-tags');
const matchScore = document.getElementById('match-score');
const matchReason = document.getElementById('match-reason');
const matchActions = document.getElementById('match-actions');
const signalsList = document.getElementById('signals');
const userInfo = document.getElementById('user-info');

let currentMatchData = null;
let signals = [];

profileForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const payload = {
    role: document.getElementById('role').value,
    industry: document.getElementById('industry').value,
    stage: document.getElementById('stage').value,
    geography: document.getElementById('geography').value
  };

  const res = await fetch('/matches', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!res.ok) {
    const error = await res.json();
    console.error(error);
    alert('Error: ' + error.detail);
    return;
  }

  const data = await res.json();
  currentMatchData = data;

  // Show match card
  profileSetup.classList.add('hidden');
  matchCard.classList.remove('hidden');

  userInfo.innerText = `${payload.role} • ${payload.industry}`;
  updateMatchCard();
});

function updateMatchCard() {
  if (!currentMatchData) return;
  const match = currentMatchData.match;

  matchName.innerText = match.name;
  matchRole.innerText = match.role;
  matchTags.innerText = match.tags.join(', ');
  matchScore.innerText = `Score: ${match.score}`;
  matchReason.innerText = currentMatchData.reason.text;

  // Actions
  matchActions.innerHTML = '';
  currentMatchData.actions.forEach(action => {
    const btn = document.createElement('button');
    btn.innerText = action.label;
    btn.className = action.primary ? 'primary-action' : 'secondary-action';
    btn.onclick = () => handleAction(action.type);
    matchActions.appendChild(btn);
  });

  updateSignals();
}

function handleAction(actionType) {
  alert(`${actionType} action performed`);
  addSignal(actionType);
}

function addSignal(actionType) {
  const text = `${actionType} action performed`;
  signals.unshift(text);
  if (signals.length > 5) signals.pop();
  updateSignals();
}

function updateSignals() {
  signalsList.innerHTML = '';
  signals.forEach(s => {
    const li = document.createElement('li');
    li.innerText = s;
    signalsList.appendChild(li);
  });
}
