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

      // Check if event id belongs to user and update button to "Leave event"
      $.post('/is-user-on-event', formInputs, (res) => {
        
        if (res === 'true') {
          console.log("This user is on the event")
          const btnTarget = `#${buttons[i].id}.btn.update-event`
          $(btnTarget).text('Leave event');  

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
        'event-id': $('.btn').val()
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