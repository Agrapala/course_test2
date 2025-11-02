import React, { useState } from 'react';
import CourseList from './components/CourseList';
import RegisterForm from './components/RegisterForm';
import './App.css';

function App() {
  const [selectedCourse, setSelectedCourse] = useState(null);

  return (
    <div className="App">
      <h1>🎓 Online Learning Platform</h1>
      {!selectedCourse ? (
        <CourseList onSelectCourse={(id) => setSelectedCourse(id)} />
      ) : (
        <RegisterForm courseId={selectedCourse} onBack={() => setSelectedCourse(null)} />
      )}
    </div>
  );
}

export default App;
