"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import { faNoteSticky, faTrashCan } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPencil } from "@fortawesome/free-solid-svg-icons";

const Sidebar = () => {
  const [notes, setNotes] = useState<NoteProps[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/notes")
      .then((res) => res.json())
      .then((data) => setNotes(data));
  }, []);

  const deleteNote = async (id: string) => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/note/${id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await res.json();
      console.log(data);
    } catch (err) {}
  };

  return (
    <aside className="flex flex-col w-[350px] text-white items-center shadow-sm shadow-black max-sm:w-full max-sm:py-4">
      <h1 className="font-bold text-4xl">Notes App</h1>
      <section className="mt-4 p-2 flex flex-col gap-2">
        {notes.map((note) => (
          <Link href={`/note/${note.id}`} key={note.id}>
            <div className="w-[325px] bg-blue-900 opacity-80 p-2 rounded-md flex items-center cursor-pointer hover:bg-blue-950 transition-all max-sm:w-full">
              <FontAwesomeIcon icon={faNoteSticky} width={25} height={25} />
              <span className="ml-2">{note.title}</span>
              <section className="flex ml-auto relative z-20">
                <FontAwesomeIcon
                  icon={faPencil}
                  width={25}
                  height={25}
                  className="cursor-pointer hover:text-blue-800 transition-all"
                  onClick={() => console.log("edit")}
                />
                <FontAwesomeIcon
                  icon={faTrashCan}
                  width={25}
                  height={25}
                  onClick={() => deleteNote(note.id)}
                  className="cursor-pointer hover:text-blue-800 transition-all"
                />
              </section>
            </div>
          </Link>
        ))}
      </section>
    </aside>
  );
};

export default Sidebar;
