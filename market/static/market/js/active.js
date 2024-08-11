// Active class for navbar


document.querySelectorAll(".nav-link").forEach((link) => {  // for each link the group 
    if (link.href === window.location.href) {   // if the current href matches a link, highlight said link 
        link.classList.add("nav-active");
       
    }
    
    
});
