$(document).ready(function(){
    // console.log($('.msgs').scrollTop());
    // var us=$('#fui').val()
    //     console.log('hello',us)
    // $('#msgform, #msg_typing_container').hide();

    $('#msg_typing_container').hide();
    $('.msgInfo').show();
    $('#Storydabba').hide(); 
        $('.chatterbox').on('click',function(){
        $('#Storydabba').show() 
        $('#msg_typing_container').show()
        $('.msgInfo').hide()

        var us=$(this).data('user');
        // iska kya kaam he
        var uid=$(this).data('user_id');
        console.log($(this))
        console.log(us)
        $('#user2').text(us)
        $('#uid').val(us);

        $('.msgs').empty()
        checkMsg();
    })
    
    
    var formmsg=document.getElementById('msgform')
    formmsg.addEventListener('submit',(e)=>{
        e.preventDefault();
        var u=$('#uid').val();
        var msg_typing=$('#msg_typing').val();
        var csrfmiddlewaretoken=$('input[name="csrfmiddlewaretoken"]').val();
        console.log(u);
        console.log(msg_typing);
        console.log(csrfmiddlewaretoken);
        $.ajax({
            url:'/messenger/',
            type:"POST",
            // isse jaa raha he
            data:{'uid':u,'csrfmiddlewaretoken':csrfmiddlewaretoken,'msg_typing':msg_typing},
            // isse aaa raha he
            success:function(data){
                console.log(data);
                checkMsg();
                $('#msg_typing').val('');
            }
        })
    })
   
   function checkMsg(){
    var sent_to_id=$('#uid').val();
    $.ajax({
        url:'/msgs/'+sent_to_id,
        type:"GET",
        success:function(data){
            console.log(data)
            $('.msgs').empty()
            // i didn't get
            data.msgs.forEach(smsg => {
                
                if(smsg.type=="receiver"){
                    $('.msgs').append(
                                '<div id="between_msges sent" class="text-start"><div class="msg_bg m-1 bg-white">'+smsg.msg+'<sub>'+smsg.timing+'</sub></div></div>'); 
                }
                else{
                    $('.msgs').append(
                        '<div id="between_msges sent" class="text-end"><div class="msg_bg m-1"> '+smsg.msg+'<sub>'+smsg.timing+'</div></div>'); 
                }
               
            });
            console.log(data.sent);
        }
    })

   }

  
    

});