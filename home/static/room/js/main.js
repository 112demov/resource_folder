import React from 'react'

function useChatScroll<T>(dep: T): React.MutableRefObject<HTMLDivElement> {
  const ref = React.useRef<HTMLDivElement>();
  React.useEffect(() => {
    if (ref.current) {
      ref.current.scrollTop = ref.current.scrollHeight;
    }
  }, [dep]);
  return ref;
}

const Chat = () => {
  const [messages , setMessages] = React.useState([])
  const ref = useChatScroll(messages)
  return(
    <div ref={ref} >
      {'#chat-messages'}
    </div>
  )
}