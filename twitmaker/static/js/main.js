document.addEventListener('DOMContentLoaded', function() {
  const monthNames = [
    "January", "February", "March",
    "April", "May", "June", "July",
    "August", "September", "October",
    "November", "December"
  ];
    let form = document.querySelector('form');
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    let formData = new FormData(this);
  
  //  console.log(formData);
  let ol = document.querySelector('.tweets');

    axios.post(
      this.action,
      formData,
    ).then(function(response) {
      console.log(response.data);
      let data = response.data;
      let li = document.createElement('li');
      let time = document.createElement('time');
      let p = document.createElement('p');
      li.className = 'tweet';
      
      var myDate = new Date(data.created_at);
      // var hola = myDate.forms
      
      zHours = myDate.getHours() > 12? myDate.getHours() - 12: myDate.getHours;
      amOrpm = myDate.getHours() > 12? 'p.m.': 'a.m.';

      let formattedDate = `${monthNames[myDate.getMonth()]} ${myDate.getDate()}, ${myDate.getFullYear()}, ${zHours}:${myDate.getMinutes()} ${amOrpm}`;    
      time.innerText = formattedDate ;
console.log(formattedDate);
      // console.log('hola', hola);
      p.innerText = data.message;
      li.appendChild(time);
      li.appendChild(p);
      ol.appendChild(li);

      let first = ol.getElementsByTagName('li')[0];
      ol.insertBefore(li, first);
      

    
    }).catch(function(error) {
      console.log(error);
    });
  });
});