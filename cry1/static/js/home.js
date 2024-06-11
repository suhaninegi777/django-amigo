function openModal() {
    document.getElementById("myModal").style.display = "block";
}

// Define closeModal function
function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

// Define displayPopup function
function displayPopup(imageUrls) {
    var popupContent = '';
    console.log("at least display popup to chala");

    // Modal HTML structure
    // popupContent += '<div class="modal-content">';
    // popupContent += '    <span class="close modal-content" onclick="closeModal()">&times;</span>';
    popupContent += '    <div class="swiper-container story__slider modal-content close" onclick="closeModal()">&times;';
    popupContent += '        <div class="story__pagination"></div>';

    popupContent += '        <div class="swiper-wrapper">';
    // popupContent += '        <div class="story__next swiper-button-next"></div>';
    // popupContent += '        <div class="story__prev swiper-button-prev"></div>';
    // Append images to swiper slides and add data attribute for imageUrls
    imageUrls.forEach(function(imageUrl, index) {
        popupContent += `            <div class="swiper-slide" data-image-url="${imageUrl}">`;
        popupContent += `                <img src="${imageUrl}" alt="Image ${index}">`;
        popupContent += '            </div>';
    });

    popupContent += '        </div>';
    
    // popupContent += '    </div>';
    // popupContent += '</div>';

    // Set the popup content to the modal
    document.getElementById("popup-content").innerHTML = popupContent;

    // Initialize Swiper
    const slider = new Swiper(".story__slider", {
        speed: 1,
        watchSlidesProgress: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false
        },
        slidesPerView: 1,
        navigation: {
            nextEl: ".story__next",
            prevEl: ".story__prev"
        },
        pagination: {
            el: ".story__pagination",
            renderBullet: function(index, className) {
                return `<div class="${className}"> <div class="swiper-pagination-progress"></div> </div>`;
            }
        },
        on: {
            autoplayTimeLeft(swiper, time, progress) {
                let currentSlide = document.querySelectorAll(".story__slider .swiper-slide")[swiper.activeIndex];
                let currentBullet = document.querySelectorAll(".story__slider .swiper-pagination-progress")[swiper.realIndex];

                // Retrieve imageUrls from data attribute
                let imageUrls = currentSlide.getAttribute('data-image-url');

                // Set default fullTime value
                let fullTime = swiper.params.autoplay.delay;

                let percentage = Math.min(Math.max(parseFloat((((fullTime - time) * 100) / fullTime).toFixed(1)), 0), 100) + "%";
                gsap.set(currentBullet, { width: percentage });
            },
            transitionEnd(swiper) {
                let allBullets = document.querySelectorAll(".story__slider .swiper-pagination-progress");
                let bulletsBefore = Array.from(allBullets).slice(0, swiper.realIndex);
                let bulletsAfter = Array.from(allBullets).slice(swiper.realIndex, allBullets.length);
                
                if (bulletsBefore.length) {
                    gsap.set(bulletsBefore, { width: "100%" });
                }
                if (bulletsAfter.length) {
                    gsap.set(bulletsAfter, { width: "0%" });
                }
            }
        }
    });

    // Open the modal
    openModal();
}
  

$('.InnerStorydabba').on('click', function () {
    var dataId = $(this).data('id');
    var dataName = $(this).data('name');
    console.log('daaaaaaaaaaaaaaaaaaaaata',dataId,dataName)
    $.ajax({
        url: '/storyShow/',
        method: 'GET',  // or 'GET', 'PUT', 'DELETE', etc. depending on your server-side endpoint
        data: {
            id: dataId,
            name: dataName
        },
        success: function (response) {
            // Handle successful response from server
            console.log('aaaaaaaaaaaaaaaaayaaaaaaaaaaaaaaaar',response);
            displayPopup(response.image_urls);
        },
        error: function (xhr, status, error) {
            // Handle error response from server
            console.error(xhr.responseText);
        }
    });
});



$(document).ready(function () {
    // ----------LIKEE_BLOCK--------------------------------------------------------
    
    // postid = $heartIcon.data('id');
    // checkLikes(postid)
    $('.fa-heart').on("click", function () {
        console.log("like dabaaya");
        var lcount = 0
        var $heartIcon = $(this); // Store reference to the heart icon

        if ($heartIcon.hasClass('liked')) {
            // lcount -= 1;
            // p = 0;
            postid = $heartIcon.data('id');
            uname = $heartIcon.data('name');

            $.ajax({
                url: '/dislike/',
                method: 'GET',
                data: { 'lcount': lcount, 'postid': postid, 'uname': uname },
                success: function (data) {
                    console.log(data);
                    $heartIcon.next('.like_counter').text(data);
                    console.log(parseInt(data))
                    $heartIcon.removeClass('liked').css({ 'color': 'white' });
                }
            });
        } else {
            // lcount += 1;
            // p = 1;
            postid = $heartIcon.data('id');
            uname = $heartIcon.data('name');

            $.ajax({
                url: '/like/',
                method: 'GET',
                data: { 'lcount': lcount, 'postid': postid, 'uname': uname },
                success: function (data) {
                    console.log(data);
                    $heartIcon.next('.like_counter').text(data);
                console.log(parseInt(data))
                $heartIcon.addClass('liked').css({ 'color': 'red' });
                }
            });
        }
        
        
    });


    // ----------COMMENT_BLOCK--------------------------------------------------------

    function checkCM(postid){
        $('#comblock.com'+postid+' .cmts').empty()
        $.ajax({
            url: '/comment/?pid='+postid,
            method: 'GET',
            success: function (data) {
                data.data.forEach(element => {
                    console.log(element.Name);
                    $('#comblock.com'+postid+' .cmts').append("<span class='pt-2 sn'><b id='SecUserName' class='fs-3 py-2'>"+element.Name+"</b><p id='commentplaced' class='p-3 pb-1'>"+element.Comment+"</p></span> <hr>")
                });
                // $('#SecUserName').text(cname);
                // $('#commentplaced').text(data.comtVal)
            },
        })
    }
        
    $('.fa-comment').on("click", function () {
        console.log("aa jaa bhhai", $('.fa-solid'))

        var $comIcon = $(this);
        var postid = $comIcon.data('id');
        var com=$('#comblock.com'+postid);
        com.toggle()
        console.log("postid", postid);
        checkCM(postid)
            
            $('#comblock.com'+postid+' #combut').on('click',function combut() {
                var comtVal = $('#comblock.com'+postid+' .comtext').val();
                crf='.csrfmiddlewaretoken'+postid
                console.log(crf)
                var csrfmiddlewaretoken=$(crf).val();
                console.log(csrfmiddlewaretoken + ' YE HE')
                console.log(comtVal,$('#comblock.com'+postid+' .comtext').val())
                $.ajax({
                    url: '/comment/',
                    method: 'POST',
                    data: { 'comtVal': comtVal, 'postid': postid ,'csrfmiddlewaretoken': csrfmiddlewaretoken },
                    success: function (data) {
                        console.log(data);
                        // $('#SecUserName').text(cname);
                        // $('#commentplaced').text(data.comtVal)
                        checkCM(postid)

                    },
                })
                console.log("form submitted")

            })
            $('#comtext').empty();
    })

});


// $('.InnerStorydabba').on('click', function () {
//     var dataId = $(this).data('id');
//     var dataName = $(this).data('name');

//     $.ajax({
//         url: 'storyShow',
//         method: 'GET',  // or 'GET', 'PUT', 'DELETE', etc. depending on your server-side endpoint

//         data: {
//             id: dataId,
//             name: dataName
//         },
//         success: function (response) {
//             // Handle successful response from server
//             console.log(response);
//             displayPopup(response.image_urls);
//         },
//         error: function (xhr, status, error) {
//             // Handle error response from server
//             console.error(xhr.responseText);
//         }
//     });
// });