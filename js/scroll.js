//add event listeners to required buttons
document.getElementById('productScroll-left').addEventListener('click', scrollPrevious, false);
document.getElementById('productScroll-right').addEventListener('click', scrollNext, false);
//Get the Snap Container
let snapContainer = document.getElementById('productSnap-Container');

//scroll Previous
function scrollPrevious(e) {
    let offset = snapContainer.children[0].clientWidth;
    snapContainer.scrollLeft -= offset
}

//scroll Next
function scrollNext(e) {
    let offset = snapContainer.children[0].clientWidth;
    snapContainer.scrollLeft += offset
}
