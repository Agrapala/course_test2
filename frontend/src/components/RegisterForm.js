import React, { useState } from 'react';
import axios from 'axios';

function RegisterForm({ courseId, onBack }) {
  const [form, setForm] = useState({ name: '', email: '' });
  const [message, setMessage] = useState('');

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post(`${process.env.REACT_APP_API_URL}/register`, {
      ...form,
      course_id: courseId
    })
      .then(() => setMessage('Registration submitted successfully!'))
      .catch(() => setMessage('Error submitting registration.'));
  };

  return (
    <div className="register-form">
      <h2>Register for Course</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Your Name" onChange={handleChange} required />
        <input type="email" name="email" placeholder="Your Email" onChange={handleChange} required />
        <button type="submit">Register</button>
        <button type="button" onClick={onBack}>Back</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default RegisterForm;
