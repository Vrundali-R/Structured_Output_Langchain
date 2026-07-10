from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing_extensions import Annotated, TypedDict, Optional,Literal

# Annotated is used to provide additional metadata about the type, which can be useful for validation or documentation purposes.
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


#schema
class PhoneReview(TypedDict):
    design: str
    display: str
    performance: Literal["excellent", "good", "average", "poor"]
    battery: str
    sentiment: Annotated[ str, "The sentiment of the review either positive, negative, or neutral."]
    key_themes: Annotated[ list[str], "A list of key themes mentioned in the review, such as design, performance, battery life, etc."]
    pros: Annotated[Optional[list[str]], "A list of positive aspects mentioned in the review."]
    Cons : Annotated[Optional[list[str]], "A list of negative aspects mentioned in the review."]


structured_model = model.with_structured_output(PhoneReview)

result = structured_model.invoke("""
    I’ve been using this phone as my primary device for nearly two months now, and the experience has honestly been a mix of impressive highs and a few frustrating compromises. The first thing that stands out is the design — it looks extremely premium with its matte finish and slim profile, and despite the large screen size, it still feels surprisingly comfortable during long usage sessions. The build quality feels solid and flagship-like, although the glossy frame tends to attract fingerprints rather quickly.

    The display is probably one of the strongest aspects of the device. Colors look vibrant without appearing overly saturated, brightness levels are excellent even under direct sunlight, and the high refresh rate makes scrolling feel incredibly fluid. Watching movies and gaming on this screen has been genuinely enjoyable. However, I did notice occasional accidental touches near the curved edges, which can get annoying at times.

    Performance-wise, the phone handles almost everything effortlessly. Multitasking, heavy gaming, video editing, and switching between apps feel smooth most of the time. Apps open quickly, and there’s barely any lag during regular usage. That said, after extended gaming sessions, the device tends to heat up noticeably near the camera module, and thermal throttling slightly affects sustained performance.

    Battery life has been decent but somewhat inconsistent. On lighter days, the phone comfortably lasts an entire day, but with heavy camera usage, gaming, and mobile data turned on continuously, I often find myself reaching for the charger by evening. Thankfully, the fast charging support is extremely convenient and compensates for this issue to some extent.

    The camera system delivers excellent results in daylight with strong dynamic range and sharp details. Portrait shots look natural, and low-light photography is surprisingly capable. However, the image processing can sometimes over-sharpen photos, and the front camera struggles a little in artificial indoor lighting conditions.

    Software experience has been mostly smooth and feature-rich, though there are occasional bugs after updates. Some pre-installed apps also feel unnecessary for a phone in this price range. Overall, despite a few shortcomings, this device still delivers a premium flagship experience with excellent display quality, strong performance, and versatile cameras, making it a solid option for power users and content consumers alike.
    

    """)

print(result)
print(type(result))
print(result["sentiment"])
