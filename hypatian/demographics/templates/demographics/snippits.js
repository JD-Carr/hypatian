const handleSubmit = async() => {
  // store the states in the form data
  const formData = new FormData();
  formData.append("name_first", formValue.name_first)
  formData.append("name_preferred", formValue.name_last)

  try {
    // make axios post request
    const response = await axios({
      method: "post",
      url: "/api/login",
      data: loginFormData,
      headers: { "Content-Type": "multipart/form-data" },
    });
  } catch(error) {
    console.log(error)
  }
}
axios.post('{{ url_for('api.patients') }}'),
  console.log('{{ form.name_first.data }}')

  .then(function (response) {
    console.log(response); // handle success
  })
  .catch(function (error) {
    console.log(error); // handle error

  });
  for (var value of formData.values()) {
     console.log(value);


function updateCell(el, row, field) {
  $(el.closest('table')).bootstrapTable('updateCell', {index: row, field: field, value: el.value})
};

function updateCell($table, index, field, newValue){

	$table.bootstrapTable("updateCell", {
		index: index,
		field: field,
		value: newValue
	});

}
rowAttributes?: (row, index) => {};
})

.on('dbl-click-cell.bs.table', function (element, field, value) {
    log('[dbl-click-cell.bs.table] field=' + field + ', value=' + value);
})

$(function(){
    $('.table tr[data-href]').each(function(){
        $(this).css('cursor','pointer').hover(
            function(){
                $(this).addClass('active');
            },
            function(){
                $(this).removeClass('active');
            }).click( function(){
                document.location = $(this).attr('data-href');
            }
        );
    });
});

<tr onclick="input" data-toggle="modal" href="#the name for my modal windows" >
 <td><label>Some value here</label></td>
</tr>

function EditCellValue(row, cell, id, value) {
    $(cell).html('<input type="text" class="form-control qbedit" placeholder="Enter Vendor Name..." value="' + value + '" />');
    $(".qbedit").focus();
    $(".qbedit").keyup(function (event) {
        if (event.keyCode == 13) {
            var vendorname = $(".qbedit").val();

            // save the edit
            $.ajax({
                type: 'PUT',
                url: '/api/AccountingAPI/' + id,
                cache: false,
                dataType: 'json',
                data: { "": vendorname }
            }).error(function (jqXHR, error, errorThrown) {
                alert(errorThrown);
            }).done(function (res) {
                // row.index is nothing. how do I get it????
                $('#mappings-table').bootstrapTable('updateCell', { index: row.index, field: 'qbvendor', value: vendorname });
            });
        }
        else if (event.keyCode == 27) {
            // cancel the edit
            $(cell).html(value);
        }
    });
}

//$form.submit( function(event) {
  //event.preventDefault();
  //console.log($('form').serialize());
  //axios.post('{{ url_for('api.patient') }}')
    //.then(function (response) {
      //console.log(response); // handle success
    //})
    //.catch(function (error) {
      //console.log(error); // handle error
    //});
//});

document.querySelector('form').addEventListener('submit', (e) => {
  const data = Object.fromEntries(new FormData(e.target).entries());
  console.log(data)
});

// Proper on form submit, not enter on a field
document.querySelector('form').addEventListener('submit', (e) => {
  const formData = new FormData(e.target);
  // Now you can use formData.get('foo'), for example.
  // Don't forget e.preventDefault() if you want to stop normal form .submission
});


var data = $('#form').serializeArray().reduce(function(obj, item) {
  obj[item.name] = item.value;
  return obj;
}, {}
);


var $form = $('form');

$(function() {
  $('form').submit(function(e) {
    e.preventDefault();
    let data = JSON.parse(JSON.stringify($($form).serializeArray()));
    axios.post('{{ url_for('api.patients') }}', data)
      .then(function (response) {
        console.log(response); // handle success
      })
      .catch(function (error) {
        console.log(error); // handle error
      })
  })
});
