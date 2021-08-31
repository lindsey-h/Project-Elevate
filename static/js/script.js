"use strict";



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
  })

  $('#sidebarToggler').on('click', () => {
    $('#evoCalendar').addClass('event-hide');
  })

  $('#eventListToggler').on('click', () => {
    $('#evoCalendar').addClass('sidebar-hide');
  })

  for (const d of data) {
    for (const u of d['users']) {
      console.log(u['fname']);
    }
    
  }

});

// $.get('/users-by-event', {index: 1}, (res) => {

//   console.log(res);

// });

// $.get('/eventsusers', {index: 2}, (res) => {
//   console.log(res);
// });

// $('#evoCalendar').removeClass('sidebar-hide');
// $("#evoCalendar").evoCalendar('toggleSidebar',true/false);
