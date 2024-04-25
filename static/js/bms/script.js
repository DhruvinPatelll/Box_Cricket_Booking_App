
// ground_detail

document.getElementById('pitch').addEventListener('change', function() {
    var selectedPitch = this.options[this.selectedIndex];
    var selectedPitchPrice = selectedPitch.getAttribute('data-price');
    document.getElementById('selectedPitchPrice').innerHTML = 'Selected Pitch Price: ₹' + selectedPitchPrice;
});

 function updatePrice() {
    var pitchDropdown = document.getElementById('pitch');
    var selectedOption = pitchDropdown.options[pitchDropdown.selectedIndex];
    var price = selectedOption.getAttribute('data-price');

    var priceInput = document.getElementById('price');
    priceInput.value = price;

    var priceDisplay = document.getElementById('priceDisplay');
    priceDisplay.innerHTML = "Price: ₹" + price;
}
function showSlotBookingForm() {
}
$(document).ready(function () {
    updatePrice();
});

function openTab(tabName) {
 // Hide all tabs
 document.querySelectorAll('.tab-content').forEach(function(tab) {
    tab.classList.remove('active-tab');
 });

 // Show the selected tab
 document.getElementById(tabName).classList.add('active-tab');
}

function showSlotBookingForm() {
 var selectedGround = document.getElementById('pitch').value;

 document.getElementById('selectedGroundInfo').innerText = 'Selected Ground : ' + selectedGround  ;

 // Hide ground selection form
 document.getElementById('tab1').classList.remove('active-tab');

 // Show slot booking form
 document.getElementById('tab2').classList.add('active-tab');
}

function changeGroundSelection() {
 // Show ground selection form
 document.getElementById('tab1').classList.add('active-tab');

 // Hide slot booking form
 document.getElementById('tab2').classList.remove('active-tab');
}

function updateSelectedGroundInfo() {
 var selectedGround = document.getElementById('pitch').value;
 document.getElementById('selectedGroundInfo').innerText = 'Selected Ground: ' + selectedGround;
}

function openTab3() {
 // Hide all tabs
 document.querySelectorAll('.tab-content').forEach(function(tab) {
    tab.classList.remove('active-tab');
 });

 // Show tab3
 document.getElementById('tab3').classList.add('active-tab');
}


// index



$(document).ready(function() {
    // Function to handle search button click
    $('#search-button').click(function() {
        var query = $('#search-input').val().trim();
        filterGrounds(query);
    });

    // Function to handle filter select change
    $('#filter-select').change(function() {
        var city = $(this).val();
        filterGrounds(city);
    });

    // Function to handle sort select change
    $('#sort-select').change(function() {
        var sortBy = $(this).val();
        sortGrounds(sortBy);
    });

    function filterGrounds(query) {
        $.ajax({
            url: '/filter/',
            type: 'GET',
            data: {
                'q': query
            },
            success: function(data) {
                $('.card-container').html(data);
            }
        });
    }

    function sortGrounds(sortBy) {
        $.ajax({
            url: '/sort/',
            type: 'GET',
            data: {
                'sort_by': sortBy
            },
            success: function(data) {
                $('.card-container').html(data);
            }
        });
    }
});


// payment

        var app = new Vue({
            delimiters: ['[[', ']]'],
            el: '#app',
            data: {
                message: 'Hello Vue!',
                name : null,
                amount : null
                
            },
            methods: {
                greet: function(name) {
                    console.log('Hello from ' + name + '!')
                },
                get : function(){
                  console.log(this.name , this.amount)
                }
            },
            watch : {
              amount(){
                  console.log(this.amount)
              }
            }
          });