const profile_pic = document.getElementById("profile_user_pic");
const modal = document.getElementById("modal");
const modal_pic = document.getElementById("profile_pic");
const caption = document.getElementById('caption');
const closeX = document.getElementById("close");

const profile_pic_cover = document.getElementById("cover_img");
const modal_cover = document.getElementById("modal_cover");
const modal_pic_cover = document.getElementById("profile_cover_pic");
const caption_cover = document.getElementById('caption_cover');
const closeX_cover = document.getElementById("close_cover");

profile_pic.addEventListener('click', () => {
    modal.style.display = "block";
    modal_pic.src = profile_pic.src;
    caption.innerHTML = profile_pic.alt;
})
profile_pic_cover.onclick = () => {
    modal_cover.style.display = "block";
    modal_pic_cover.src = profile_pic_cover.src;
    caption_cover.innerHTML = profile_pic_cover.alt;
}

closeX.onclick = () => {
    modal.style.display = "none";
}
closeX_cover.onclick = () => {
    modal_cover.style.display = "none";
}