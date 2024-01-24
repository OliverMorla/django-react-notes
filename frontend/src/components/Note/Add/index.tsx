"use client";
import { useState } from "react";

const CreateNote = () => {
  const [noteInput, setNoteInput] = useState({
    title: "",
    body: "",
  });

  const createNote = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/notes/", {
        method: "POST",
        body: JSON.stringify(noteInput),
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await res.json();
      console.log(data);
    } catch (err) {}
  };

  return (
    <section className="h-[350px] w-full p-10 flex flex-col gap-4 shadow-gray-400 shadow-sm">
      <h1 className="text-4xl">Add a Note</h1>
      <input
        className="bg-transparent outline-none"
        placeholder="Title"
        name="title"
        onChange={(e) =>
          setNoteInput({ ...noteInput, [e.target.name]: e.target.value })
        }
      />
      <input
        className="bg-transparent outline-none"
        placeholder="Take a note..."
        name="body"
        onChange={(e) =>
          setNoteInput({ ...noteInput, [e.target.name]: e.target.value })
        }
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            createNote();
          }
        }}
      />
    </section>
  );
};

export default CreateNote;
