"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import { faNoteSticky } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const Sidebar = () => {
  const [notes, setNotes] = useState<NoteProps[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/notes-db/")
      .then((res) => res.json())
      .then((data) => setNotes(data));
  }, []);

  return (
    <aside className="flex flex-col w-[350px] text-white items-center shadow-sm shadow-black">
      <h1 className="font-bold text-4xl">Notes App</h1>
      <section className="mt-4 p-2 flex flex-col gap-2">
        {notes.map((note) => (
          <Link href={"/"} key={note.id}>
            <div className="w-[325px] bg-blue-900 opacity-80 p-2 rounded-md flex items-center cursor-pointer hover:bg-blue-950 transition-all">
              <FontAwesomeIcon icon={faNoteSticky} width={25} height={25} />
              <span className="ml-2">{note.title}</span>
            </div>
          </Link>
        ))}
      </section>
    </aside>
  );
};

export default Sidebar;
