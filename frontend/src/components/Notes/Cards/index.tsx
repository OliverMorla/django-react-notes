import { faTrashCan } from "@fortawesome/free-regular-svg-icons";
import { faPencil } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const Note = ({ id, title, body, createdAt, updatedAt }: NoteProps) => {
  return (
    <div className="w-[325px] h-[275px] p-4 shadow-sm shadow-black flex flex-col justify-between hover:scale-105 transition-all cursor-pointer">
      <section className="flex justify-between items-center">
        <h4 className="text-2xl">{title}</h4>
        <section className="flex gap-2 items-center">
          <FontAwesomeIcon icon={faPencil} width={25} height={25} className="cursor-pointer hover:text-blue-800 transition-all"/>
          <FontAwesomeIcon icon={faTrashCan} width={25} height={25} className="cursor-pointer hover:text-blue-800 transition-all"/>
        </section>
      </section>
      <p>{body}</p>
      <section className="flex opacity-60 justify-between">
        <span>{new Date(createdAt).toLocaleDateString()}</span>
        <span>{new Date(updatedAt).toLocaleDateString()}</span>
      </section>
    </div>
  );
};

export default Note;
