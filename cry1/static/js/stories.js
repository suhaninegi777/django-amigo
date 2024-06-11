// $(document).ready(function () {
//     console.log("start")
//     // \ -----------------TEXT STORY------------------------
//         $(text_story).on('click', function () {
//             $('#photos_story').css({'display':'none'})
//             console.log("display none")
//             $('#for_text_story').css({'display':'block'})

//             $('#myTextarea').on('input', function () {
//                 const story_content=$(this).val()
//                 const digit = story_content.length;
//                 $('#wordCount').text(digit + (digit === 1 ? ' word' : ' digit'));
//                 console.log("yes  working")
        
//                 if (digit > 100) {
//                     this.val(story_content.substring(0, story_content.lastIndexOf(' ', 400)));
//                     $('#wordCount').css({ 'color': 'red' })
//                     $('#wordCount').text('100 digit maximum reached');
        
//                 }
//                 $('#story_watch').html(story_content)
        
//             });
//         })
// // ----------------------------IMAGE STORY----------------------------
// $(photos_story).on('click', function () {
//     const story_content=$(this).val()
//     let file=''
//     $('#file_img').on('change',(e)=>{
//         file=e.target.files[0]
//         // "{% static 'IMAGES/wow.jpg' %}"
//         $('#story_watch').append(`<img src="{% static 'IMAGES/${file.name}' %}" alt='hello' >`)
//         $('#datagoing').val(file.name)
//     })
//     if(file.name!=''){

//         var file_URL=file.name
//         console.log('url of selected files')
//         console.log(file.name)
//     }
//     else{
//         console.log("not running")
//     }
//     // $("#container")
   
//     // $('#story_watch').html(story_content)
//     // $("img").attr("src",{file_URL});

// })

    
// });