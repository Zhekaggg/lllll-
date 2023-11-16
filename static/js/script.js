document.addEventListener('DOMContentLoaded', function () {
    const calendarContainer = document.querySelector('.calendar-container');
    const currentMonthElement = document.getElementById('currentMonth');
    const calendarElement = document.getElementById('calendar');
    const eventListElement = document.getElementById('eventList');
    const prevMonthBtn = document.getElementById('prevMonthBtn');
    const nextMonthBtn = document.getElementById('nextMonthBtn');

    let currentDate = new Date();

    function renderCalendar() {
        const firstDayOfMonth = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
        const lastDayOfMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);
        const lastDayOfPrevMonth = new Date(currentDate.getFullYear(), currentDate.getMonth(), 0);

        const startDay = firstDayOfMonth.getDay();
        const lastDay = lastDayOfMonth.getDate();
        const lastDayPrevMonth = lastDayOfPrevMonth.getDate();

        currentMonthElement.textContent = new Intl.DateTimeFormat('ru-RU', { month: 'long', year: 'numeric' }).format(currentDate);

        let dayIndex = 0;
        calendarElement.innerHTML = '';

        // Add previous month days
        for (let i = startDay - 1; i >= 0; i--) {
            const dayElement = createDayElement(lastDayPrevMonth - i, true);
            calendarElement.appendChild(dayElement);
        }

        // Add current month days
        for (let i = 1; i <= lastDay; i++) {
            const dayElement = createDayElement(i, false);
            calendarElement.appendChild(dayElement);
        }

        // Add next month days
        const totalDays = startDay + lastDay;
        const remainingDays = 42 - totalDays;

        for (let i = 1; i <= remainingDays; i++) {
            const dayElement = createDayElement(i, true);
            calendarElement.appendChild(dayElement);
        }
    }

    function createDayElement(day, isDisabled) {
        const dayElement = document.createElement('div');
        dayElement.classList.add('day');
        dayElement.textContent = day;
        if (!isDisabled) {
            dayElement.addEventListener('click', () => showEvents(day));
        } else {
            dayElement.classList.add('disabled');
        }

        // Добавляем обводку для текущего дня
        if (
            currentDate.getFullYear() === new Date().getFullYear() &&
            currentDate.getMonth() === new Date().getMonth() &&
            day === new Date().getDate()
        ) {
            dayElement.classList.add('today');
        }

        return dayElement;
    }

    function showEvents(day) {
        const events = getEventsFromDatabase(currentDate.getFullYear(), currentDate.getMonth() + 1, day);

        const formattedEvents = events.map(event => {
            return `<div class="event">${event.title}</div>`;
        });

        eventListElement.innerHTML = formattedEvents.join('');
    }

    function getEventsFromDatabase(year, month, day) {
        // Здесь вы должны реализовать логику получения событий из базы данных
        // для выбранной даты (year, month, day). Это может включать в себя AJAX запросы,
        // использование серверной части приложения и т. д.
        // Замените этот код на ваш реальный код для работы с базой данных.

        // В данном примере возвращается массив событий для иллюстрации.
        // Ваш код должен быть адаптирован к вашей базе данных и бэкенд-технологиям.

        const events = [
            { title: 'Событие 1', time: '10:00' },
            { title: 'Событие 2', time: '14:30' },
            // Добавьте больше событий при необходимости
        ];

        return events;
    }

    function updateCalendar() {
        renderCalendar();
        showEvents(currentDate.getDate());
    }

    prevMonthBtn.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        updateCalendar();
    });

    nextMonthBtn.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        updateCalendar();
    });

    // Инициализация календаря
    updateCalendar();
});
