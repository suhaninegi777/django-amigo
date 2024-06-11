$(document).ready(function () {
    console.log("hi")
    $(".editbutton").click(function () {
        console.log("Button clicked!");
        $(".profilepost").css({ display: "none"})
        $(".editpage").css({ display: "block" })
        // if onclick exit&&submit buttton profilepost editpage:diplay-none
    });

    $(".postbtn").click(function () {
        console.log("Button clicked!");
        $(".profilepost").css({ display: "block"})
        $(".editpage").css({ display: "none" })
        // if onclick exit&&submit buttton profilepost editpage:diplay-none
    });

    function showStory() {
        $(this).html(`<a href="/StoryView/"></a>`)
    }
    $(".exit_but").click(function () {
        console.log("hit exit button")
        $(".profilepost").css({ display: "block" })
        $(".editpage").css({ display: "none" })
        window.location.assign('/profile/')
        console.log("hit exit button")
    });
    // $('#imgpreview').css({'display':none})
    $('#clickaddpost').on('click',()=>{
        // $('#imgpreview').css({'display':block})

        $('.cross').on('click', ()=>{
            $('.post_absolute_part').css({display:'none'})
            $('.post_absolute_part').hide()
        })
        $('.post_absolute_part').css({ display: 'block' });
        $('#adpost').change(function (e) {
            $('label').hide()
            // $('clickaddpost').hide();
            file = e.target.files[0]
            console.log(file)
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => {
                // var path = "{% static 'IMAGES/' %}";
                var url = reader.result;
                $('#imgpreview').attr('src', url);
                $('#imgpreview').attr('alt', url);
                $('#imgpreview').css({ 'height': '75vh', 'width': '80%' });
            };
            })
        

    })
    $('.imgclick').on('click',function(){
        $('.cross').on('click', ()=>{
            $('#showpost').css({display:'none'})
            $('#showpost').hide()
        })
        url=$(this).attr('data-image')
        caption=$(this).attr('data-caption')
        console.log('caption',caption)
        // var path = "{% static 'IMAGES/' %}";
        $('#showpost').css({display:'block'})
        $('#showpost img').attr('src',url)
        $('#img_caption').text(caption)
    })

    
})