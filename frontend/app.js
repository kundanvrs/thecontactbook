console.log("JavaScript asset pipeline connected successfully!");

async function fetchContacts() {
    const res = await fetch('/api/contacts');
    const contacts = await res.json();
    const container = document.getElementById('contactList');
    
    if (contacts.length === 0) {
        container.innerHTML = '<p style="color: #888; text-align:center;">No contacts saved yet.</p>';
        return;
    }

    container.innerHTML = contacts.map(c => `
        <div class="contact-card">
            <h3>👤 ${c.name}</h3>
            <p>✉️ ${c.email}</p>
            <p>📞 ${c.phone}</p>
        </div>
    `).join('');
}

async function addContact() {
    const name = document.getElementById('contactName').value;
    const email = document.getElementById('contactEmail').value;
    const phone = document.getElementById('contactPhone').value;

    if (!name || !email || !phone) {
        alert("Please fill out all fields.");
        return;
    }

    const response = await fetch('/api/contacts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, phone })
    });

    if (response.ok) {
        // Clear input boxes
        document.getElementById('contactName').value = '';
        document.getElementById('contactEmail').value = '';
        document.getElementById('contactPhone').value = '';
        fetchContacts();
    } else {
        const err = await response.json();
        alert(`Error: ${err.detail}`);
    }
}

// Render data on initial load
window.onload = fetchContacts;