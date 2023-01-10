const slugInput = document.querySelector('input[name=slug]');
const titleInput = document.querySelector('input[name=title]');


const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-')         //replace & with -and-
    .replace(/[\s\W-]+/g, '-')      //replace space, nonword char and dashes with -
};

titleInput.addEventListener('keyup', (e)=>{
    slugInput.setAttribute('value', slugify(titleInput.value));
});