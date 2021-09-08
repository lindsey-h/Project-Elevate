"use strict";
// import React from 'react';
// import ReactDOM from 'react-dom';


$.get('/event-data', (data) => {

  $('#evoCalendar').evoCalendar({
    calendarEvents: data,
    todayHighlight: true,
    sidebarToggler: true,
    sidebarDisplayDefault: false,
  })

  .on('selectDate', function(newDate, oldDate) {
    
    $('#evoCalendar').removeClass('event-hide');
    $('#evoCalendar').addClass('sidebar-hide');
    // Get request for user id
    // Is user on event 
    // Button text = Leave event 
    
    const buttons = $(".btn.update-event")

    for (let i = 0; i < buttons.length; i++) { 
    
      // formInputs[buttons[i].id] = buttons[i].value
      // // 'btn6': '6'
      // // 'btn7': '7'
      const formInputs = {

        'event-id': buttons[i].value

      };

      $.post('/is-user-on-event', formInputs, (res) => {
        
        if (res === 'true') {
          console.log("This user is on the event")
          const btnTarget = `#${buttons[i].id}.btn.update-event`
          $(btnTarget).text('Leave event');  

        }

      });

    };

    


    
    // Add or remove a user from an event
    $(`.btn.update-event`).on('click', (evt) => {

      const btnId = evt.target.id
      const btnTarget = `#${btnId}.btn.update-event`
      const btnVal = $('.btn').val();
      
      const formInputs = {
        'event-id': $('.btn').val()
      };

      if ($(btnTarget).text() === 'Join event') {

        $.post('/add-user-to-event', formInputs, (res) => {
          console.log(res);
          $(`.event-desc#${btnVal}`).append(", "+res)
        });

        $(btnTarget).text('Leave event');

      }

      else if ($(btnTarget).text() === 'Leave event'){

        $.post('/remove-user-from-event', formInputs, (res) => {
          let users = $(`#${btnVal}.event-desc`).text()
          const removedUser = users.replace(`, ${res}`, '')
          $(`#${btnVal}.event-desc`).text(removedUser)
        });

        $(btnTarget).text('Join event');

      }
    
    });

  })

  // ? ASK IN QUEUE ?
  // How to have this load without clicking on an event date 
  $(document).ready(function(){
    $(".btn").click(function(){
      console.log('clicked on me');
    });
  });

  // .on('selectEvent', function(activeEvent) {
  //   $('div.event-info').html("helloooooo");
  // })

  $('#sidebarToggler').on('click', () => {
    $('#evoCalendar').addClass('event-hide');
  })

  $('#eventListToggler').on('click', () => {
    $('#evoCalendar').addClass('sidebar-hide');
  })

  // $('.btn').on('click', () => {
  
  //   console.log('clicked on me');
    
  // });

});




  // $('div.event-container').on('mouseover', function () {
  //   alert("hi");
  // })

// $.get('/users-by-event', {index: 1}, (res) => {

//   console.log(res);

// });

// $.get('/eventsusers', {index: 2}, (res) => {
//   console.log(res);
// });

// $('#evoCalendar').removeClass('sidebar-hide');
// $("#evoCalendar").evoCalendar('toggleSidebar',true/false);


// ReactDOM.render(
//   <h1>This is an example.</h1>, 
//   document.getElementById('event-button')
// );