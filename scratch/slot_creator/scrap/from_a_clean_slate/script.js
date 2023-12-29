


function getStartTimeInputValue() {
    return (document.getElementById('startDateTime')).value;
}


function getEndTimeInputValue() {
    return (document.getElementById('endDateTime')).value;
}


function getQuantityInputValue() {
    return parseInt((document.getElementById('quantity')).value, 10);
}


function getRoleInputValue() {
    return (document.getElementById('role')).value;
}


function calculateDuration(start, end) {
    const startDate = new Date(start).getMilliseconds();
    const endDate = new Date(end).getMilliseconds();
    const durationInMilliseconds = endDate - startDate;
    const durationInHours = durationInMilliseconds / (1000 * 60 * 60);
    return durationInHours.toFixed(2);
}


function updateDuration(row) {
    const startDateTime = row.cells[0].querySelector('input').value;
    const endDateTime = row.cells[1].querySelector('input').value;
    const durationCell = row.cells[3];

    const duration = calculateDuration(startDateTime, endDateTime);
    durationCell.textContent = duration;
} 


function makeEditableCell(value, inputType, inputEvents) {
    const input = document.createElement('input');
    input.type = inputType;
    input.value = value;
    inputEvents.forEach(event =>
        input.addEventListener('input', event)
    );
    return input;
}

function makeDeleteButton(row) {
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', () => {
        row.remove();
    });
    return deleteButton;
}


function addRow(startDateTime, endDateTime, role) {
    const timeSlotsTableBody = document.getElementById('timeSlotsTableBody');
    const row = timeSlotsTableBody.insertRow(-1);
    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);
    const cell3 = row.insertCell(2);
    const cell4 = row.insertCell(3);
    const cell5 = row.insertCell(4);

    const onEditEvents = [
        () => updateDuration(row)
    ];

    // Create editable input fields
    // Add start
    const startInput = makeEditableCell(
        startDateTime, 'text', onEditEvents);
    cell1.appendChild(startInput);

    // Add end
    const endInput = makeEditableCell(
        endDateTime, 'text', onEditEvents);
    cell2.appendChild(endInput);

    // Add role
    const roleInput = makeEditableCell(
        role, 'text', onEditEvents);
    cell3.appendChild(roleInput);

    // Calculate and display the duration
    const duration = calculateDuration(startDateTime, endDateTime);
    cell4.textContent = duration;

    // Add delete button
    const deleteButton = makeDeleteButton(row);
    cell5.appendChild(deleteButton)
}


function showMessage(message) {
    const messageElement = document.getElementById('message');
    if (messageElement) {
        messageElement.textContent = message;
        messageElement.style.display = 'block';
    }
}

    
function isInputValid() {
    const startDateTime = getStartTimeInputValue();
    const endDateTime = getEndTimeInputValue();
    const quantity = getQuantityInputValue();
    const role = getRoleInputValue();

    return startDateTime && endDateTime && !isNaN(quantity) && quantity > 0 && role;
}

// eslint-disable-next-line no-unused-vars
function addTimeSlots() {
    const startDateTime = getStartTimeInputValue();
    const endDateTime = getEndTimeInputValue();
    const quantity = getQuantityInputValue();
    const role = getRoleInputValue();

    if (!isInputValid()) {
        showMessage('Please enter valid values for start date/time, end date/time, quantity, and role.')
    }

    for (let i = 0; i < quantity; i++) {
        addRow(startDateTime, endDateTime, role);
    }
}     