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
    $('.btn').on('click', () => {
  
      console.log($('.btn').val());
    
    });
  })

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