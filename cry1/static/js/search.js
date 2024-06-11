$(document).ready(function () {
  var Sval=''
  $('.sbox').hide();
  $('#search').on('input', function () {
    Sval = $('#search').val()
    console.log(Sval)
    if(Sval.length>0){
      $.ajax({
        url: '/viewsearch/?searchdata='+Sval,
        type: 'GET',
        // data: { 'searchvalue': Sval },
        success: function (data) {
          $('.sbox .res').empty();
          data.res.forEach(element => {
           
            console.log(element.uname)
            $('.sbox').show();
            $('.sbox .res').append('<a href="'+element.url+'" class="py-2 border-bottom text-decoration-none">'+element.uname+'</a>');
          });
          // checksearch_showlist()
        }
      })
    }
    else{
      $('.sbox .res').empty();
    }
  
});
  function checksearch_showlist() {
    $.ajax({
      url: '/search/',
      type: 'GET',
      success: function (data) {
        console.log(data)
        data.filteredata.forEach(element => {
          $('ul').append(`<li>${filtereddata}</li>`)
        });
        
      }
    })
  }
})