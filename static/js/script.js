/* jshint esversion: 8, jquery: true */


// JavaScript code updated to be more modular and easier to maintain.
// Help from Rodrigo Caldato: https://www.linkedin.com/in/rodrigo-caldato-391137115/


// Function to initialize datepicker widget with specific settings
function initializeDatepicker() {
    const datepicker = $("#datepicker");

    datepicker.datepicker({
        dateFormat: "MM d, yy",
        minDate: 0,
        maxDate: "+12M +0D",
        showAnim: "fold",
    }).datepicker("setDate", '0');
}

// Function to filter booking table by given criteria
function filterTable(criteria, selector) {
    const resultRows = document.querySelectorAll(".booking-row");
    const filterValue = $(selector).text();

    resultRows.forEach(row => {
        row.classList.add("d-none");
        if (row.innerText.includes(filterValue)) {
            row.classList.remove("d-none");
        }
    });
}

// Function to remove "d-none" class from all rows
function removeFilter() {
    $(".booking-row").removeClass("d-none");
}

// Function to handle button click and update selected value
function handleButtonClick() {
    const val = $(this).val();
    $('.btn').removeClass('selected');
    $(this).addClass('selected');
    $('.selectedVal').val(val);
}

// Document ready function
$(document).ready(function () {
    initializeDatepicker();

    $("#datepicker").on("change", function () {
        filterTable("date", "#datepicker");
    });

    $("#table-filter-user").on("click", function () {
        filterTable("user", "#current-user");
    });

    $("#refresh-table").on("click", removeFilter);
    $(".btn").on("click", handleButtonClick);
});