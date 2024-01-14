/* jshint esversion: 8, jquery: true */

/**
 * Initialize datepicker widget with specific settings
 */
 function initializeDatepicker() {
    const datepicker = $("#datepicker");
    
    datepicker.datepicker({
        dateFormat: "MM d, yy",
        minDate: 0,
        maxDate: "+12M +0D",
        beforeShowDay: $.datepicker.noWeekends
    });

    datepicker.datepicker("option", "showAnim", "fold");
    datepicker.datepicker("setDate", '0');
}

/**
 * Filter booking table by datepicker value
 */
function filterResults() {
    const resultRows = document.querySelectorAll(".booking-row");
    const filterData = $("#datepicker").val();

    resultRows.forEach(row => {
        row.classList.add("d-none");
        if (row.innerText.includes(filterData)) {
            row.classList.remove("d-none");
        }
    });
}

/**
 * Filter view-booking-table by current user
 */
function myBookingsFilter() {
    const resultRows = document.querySelectorAll(".booking-row");
    const filterUser = $("#current-user").text();

    resultRows.forEach(row => {
        row.classList.add("d-none");
        if (row.innerText.includes(filterUser)) {
            row.classList.remove("d-none");
        }
    });
}

/**
 * Unfilter booking table by removing "d-none" class
 */
function removeFilter() {
    const resultRows = document.querySelectorAll(".booking-row");

    resultRows.forEach(row => {
        row.classList.remove("d-none");
    });
}

/**
 * Handle button click to update selected value
 */
function handleButtonClick() {
    const val = $(this).val();
    $('.btn').removeClass('selected');
    $(this).addClass('selected');
    $('.selectedVal').val(val);
}

// Document ready function
$(document).ready(function () {
    initializeDatepicker();

    $("#datepicker").on("change", filterResults);
    $("#table-filter-user").on("click", myBookingsFilter);
    $("#refresh-table").on("click", removeFilter);
    $(".btn").on("click", handleButtonClick);
});