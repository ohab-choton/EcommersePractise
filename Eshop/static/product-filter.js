$(document).ready(function () {
    $(".ajx-loader").hide();
    
    $(".filter-checkbox").on('click', function () {
        var _filterObj = {};

        $(".filter-checkbox:checked").each(function () {
            var _filterKey = $(this).data('filter');  // Get filter type (color, category, etc.)
            
            if (!_filterObj[_filterKey]) {
                _filterObj[_filterKey] = [];  // Initialize as an array
            }
            
            _filterObj[_filterKey].push($(this).val()); // Add selected values
        });

        $.ajax({
            url: '/filter-data/',
            data: _filterObj,
            dataType: 'json',
            beforeSend: function () {
                $(".ajx-loader").show();
            },
            success: function (res) {
                console.log(res);
                $(".ajx-loader").hide();
                $("#filteredProducts").html(res.data);  // Correctly insert filtered products
            }
        });
    });
});
