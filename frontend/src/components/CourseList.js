import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CourseList({ onSelectCourse }) {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}/courses`)
      .then(res => setCourses(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="course-list">
      <h2>Available Courses</h2>
      <div className="grid">
        {courses.map(course => (
          <div key={course.id} className="card">
            <img src={course.image} alt={course.title} />
            <h3>{course.title}</h3>
            <p>{course.description}</p>
            <button onClick={() => onSelectCourse(course.id)}>Register</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CourseList;
