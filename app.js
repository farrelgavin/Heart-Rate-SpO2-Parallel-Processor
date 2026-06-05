// ── Navigation ──────────────────────────────────────────────
const navItems = document.querySelectorAll('.nav-item');
const pages    = document.querySelectorAll('.page');

function navigate(targetId) {
  pages.forEach(p => p.classList.remove('active'));
  navItems.forEach(n => n.classList.remove('active'));

  const targetPage = document.getElementById(targetId);
  if (targetPage) targetPage.classList.add('active');

  const targetNav = document.querySelector(`[data-page="${targetId}"]`);
  if (targetNav) targetNav.classList.add('active');
}

navItems.forEach(item => {
  item.addEventListener('click', () => navigate(item.dataset.page));
});

// ── Search ───────────────────────────────────────────────────
const searchInput = document.getElementById('search');

searchInput.addEventListener('input', () => {
  const q = searchInput.value.toLowerCase().trim();
  navItems.forEach(item => {
    const text = item.textContent.toLowerCase();
    item.style.display = (!q || text.includes(q)) ? '' : 'none';
  });
});

// ── Init ─────────────────────────────────────────────────────
navigate('home');
