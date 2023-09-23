import React, { useState } from "react";
import { v4 as uuid } from 'uuid';

function NewBoxForm({ createBox }) {
    const [formData, setFormData] = useState({
      height: "",
      width: "",
      backgroundColor: ""
    });
  
    const handleChange = event => {
      const { name, value } = event.target;
      setFormData(formData => ({
        ...formData,
        [name]: value
      }));
    };
  
    const gatherInput = event => {
      event.preventDefault();
      createBox({ ...formData, id: uuid() });
      setFormData({ height: "", width: "", backgroundColor: "" });
    };
  
    return (
      <div>
        <form onSubmit={gatherInput}>
          <div>
            <label htmlFor="height">Height</label>
            <input
              onChange={handleChange}
              type="text"
              name="height"
              id="height"
              value={formData.height}
            />
          </div>
          <div>
            <label htmlFor="width">Width</label>
            <input
              onChange={handleChange}
              type="text"
              name="width"
              id="width"
              value={formData.width}
            />
          </div>
          <div>
            <label htmlFor="backgroundColor">Background Color</label>
            <input
              onChange={handleChange}
              type="text"
              name="backgroundColor"
              id="backgroundColor"
              value={formData.backgroundColor}
            />
          </div>
          <button id="newBoxButton">Add a new box!</button>
        </form>
      </div>
    );
  }
  
  export default NewBoxForm;