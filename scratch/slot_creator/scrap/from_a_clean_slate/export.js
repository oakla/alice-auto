function getTableHeaders(){
    headers = document.getElementById('timeSlotHeaderRow').querySelectorAll('th');
    headers = Array.from(headers).map(th => th.textContent);
    return headers;
}

function getTableRows(){
    const table = document.getElementById('timeSlotsTableBody');
    const rows = table.rows;
    const data = [];
    for (let i = 0; i < rows.length; i++) {
        const row = rows[i];
        const cells = row.cells;
        const start = cells[0].querySelector('input').value;
        const end = cells[1].querySelector('input').value;
        const role = cells[2].querySelector('input').value;
        // const duration = cells[3].textContent;
        data.push({
            start,
            end,
            role,
            // duration,
        });
    }
    return data;
}

function exportToCSV() {
    
    // const headers = getTableHeaders();
    const data = getTableRows();

    const csvContent = [];
    csvContent.push("start,end,role");
    for (let i = 0; i < data.length; i++) {
        const row = data[i];
        const values = Object.values(row);
        csvContent.push(values.join(','));
    }

    // Create a Blob containing the CSV data
    const csvData = new Blob([csvContent.join('\n')], { type: 'text/csv' });

    // Create a download link and trigger a click event to download the file
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(csvData);
    downloadLink.download = 'time_slots.csv';
    downloadLink.click();

}