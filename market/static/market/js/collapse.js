// Collapse section

// selecting the container for each faq
let faqs = document.querySelectorAll(".faq");

//toggling the css class 'active' in order to use accordian
  faqs.forEach(faq => {
    faq.addEventListener("click", () => {
      faq.classList.toggle("active")
    })

  })