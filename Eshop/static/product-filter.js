$(document).ready(function () {
    $(".ajx-loader").hide();
    $(".filter-checkbox").on('click', function () {
        var _filterObj = {};
        $(".filter-checkbox").each(function () {
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
                return el.value;
            });
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
