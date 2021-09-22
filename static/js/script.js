"use strict";
// import React from 'react';
// import ReactDOM from 'react-dom';
let url = window.location.href.split("/");
let uId = url[url.length - 1];
let isUserPage = url[url.length - 2];



$.get('/event-data/' + uId, (data) => {

  // Create the calendar

  $('#evoCalendar').evoCalendar({
    calendarEvents: data,
    todayHighlight: true,
    sidebarToggler: true,
    sidebarDisplayDefault: false,
  })

  // Toggle the side bar and event bar so only one shows at a time

  .on('selectDate', function(newDate, oldDate) {
    
    $('#evoCalendar').removeClass('event-hide');
    $('#evoCalendar').addClass('sidebar-hide');


    // -----------------------------------------------
    // Check if current user belongs to visible events
    // -----------------------------------------------
    
    const buttons = $(".btn.update-event")
    // ex: button.id = btn6
    // ex: button.value = 6

    // Loop over button objects 
    for (let i = 0; i < buttons.length; i++) { 

      // Event id and button values are the same
      const formInputs = {

        'event-id': buttons[i].value

      };

      console.log(`form inputs are: ${formInputs["event-id"]}`)

      // Check if event id belongs to user and update button to "Leave event"
      $.post('/is-user-on-event', formInputs, (res) => {

        console.log(res);
        const btnTarget = `#${buttons[i].id}.btn.update-event`
        
        // if they are an attendee 
        if (res === 'true') {
          console.log("This user is on the event")
          $(btnTarget).text('Leave event');  

        }

        // if they are the author and not on a /users page 
        else if (res === 'false' && isUserPage !== 'users') {
          $(btnTarget).text('Delete event');
        }

      });

    };


    // ------------------------------------
    // Add or remove a user from an event
    // ------------------------------------

    $(`.btn.update-event`).on('click', (evt) => {

      const btnId = evt.target.id
      const btnTarget = `#${btnId}.btn.update-event`
      const btnVal = $(`#${btnId}`).val();
      
      const formInputs = {
        'event-id': btnVal
      };

      if ($(btnTarget).text() === 'Join event') {

        $.post('/add-user-to-event', formInputs, (res) => {
          console.log(res);
          $(`.event-desc#${btnVal}`).append(",  "+res)
        });

        $(btnTarget).text('Leave event');

      }

      else if ($(btnTarget).text() === 'Leave event'){

        $.post('/remove-user-from-event', formInputs, (res) => {
          
          let users = $(`#${btnVal}.event-desc`).text()
          console.log(`In the remove event descript is: ${users}`)
          
          const removedUser = users.replace(`,  ${res}`, '')
          console.log(`Removed text is: ${removedUser}`)
          
          $(`#${btnVal}.event-desc`).text(removedUser)
        });

        $(btnTarget).text('Join event');

      }

      else if ($(btnTarget).text() === 'Delete event'){

        $.post('/delete-event', formInputs, (res) => {
          
          $(`#btn${btnVal}`).parent().parent().hide()
        });

      }
    
    });

    
 

  })

  $("#evoCalendar.orange").evoCalendar('setTheme', 'Orange Coral');


  $( document ).ready(function() {
    // Handler for .ready() called.
  
  
  });


  $('#sidebarToggler').on('click', () => {
    $('#evoCalendar').addClass('event-hide');
  })

  $('#eventListToggler').on('click', () => {
    $('#evoCalendar').addClass('sidebar-hide');
  })


});

//credit https://stackoverflow.com/questions/4801561/flash-message-fade-effect

$(function() {
  $('.flash-msg').delay(500).fadeIn('normal', function() {
     $(this).delay(2000).fadeOut();
  });
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