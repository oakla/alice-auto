$(document).ready(function () {
    const uploadForm = $('#uploadForm');
    const messageDiv = $('#message');
    const dataTable = $('#dataTable');

    uploadForm.submit(function (event) {
        event.preventDefault();

        const formData = new FormData(this);

        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (jsonData) {
                // Clear previous data
                dataTable.empty();

                // Display data in the table
                const headersRow = $('<tr></tr>');
                Object.keys(jsonData[0]).forEach(function (header) {
                    const th = $('<th></th>').text(header);
                    headersRow.append(th);
                });
                dataTable.append(headersRow);

                jsonData.forEach(function (rowData) {
                    const row = $('<tr></tr>');
                    Object.values(rowData).forEach(function (value) {
                        const td = $('<td></td>').text(value);
                        row.append(td);
                    });
                    dataTable.append(row);
                });

                // Clear previous messages
                messageDiv.text('');
            },
            error: function (xhr, status, error) {
                console.error('Error uploading CSV:', error);
                messageDiv.text('Error uploading CSV. Please try again.');
            }
        });
    });
});
