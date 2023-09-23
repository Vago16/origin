import React from "react";

function Box({
  id,
  handleRemove,
  width = 5,
  height = 5,
  backgroundColor = "blue"
}) {
  const remove = () => handleRemove(id);
  return (
    <div>
      <div
        style={{
          height: `${height}`,
          width: `${width}`,
          backgroundColor
        }}
      />
      <button onClick={remove}>Remove this box</button>
    </div>
  );
}

export default Box;