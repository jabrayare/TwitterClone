const footerModal = document.getElementById("user_footer_modal")
const footer = document.getElementById("user_footer");
footer.addEventListener('click', () => {
    footerModal.style.display = "block";
})

function closeModal() {
    document.querySelector(".user_footer_modal").style.display = "none"
}
window.addEventListener(
    "mouseup",
    function(event) {
        const modalBox = document.getElementById("user_footer_modal");
        if (event.target != modalBox && event.target.parentNode.nodeName != 'DIV') {
            modalBox.style.display = 'none';
        }
        event.preventDefault()
    },
    false
)