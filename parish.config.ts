/**
 * Parish Configuration
 * =====================
 * This is the ONLY file a parish needs to edit to customize their site.
 * Everything else is template code.
 */

export const parish = {
  // Identity
  name: "Dormition of the Most Holy Mother of God",
  nameUk: "Успіння Пресвятої Богородиці",
  shortName: "Dormition Parish",
  eparchy: "Ukrainian Catholic Eparchy of Edmonton",
  rite: "Byzantine (Ukrainian)",

  // Location
  address: {
    street: "15603 104 Avenue NW",
    city: "Edmonton",
    province: "Alberta",
    postalCode: "T5P 4G5",
    country: "Canada",
    mapUrl: "https://maps.google.com/?q=15603+104+Avenue+NW+Edmonton+AB+T5P+4G5",
    mapEmbed: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2370.5!2d-113.545!3d53.555!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNTPCsDMzJzE4LjAiTiAxMTPCsDMyJzQyLjAiVw!5e0!3m2!1sen!2sca!4v1600000000000",
  },

  // Contact
  phone: "780-489-8868",
  email: "dormitionparish@gmail.com",
  website: "https://dormition.eeparchy.com",

  // Services — the most important data on the site
  services: {
    confession: {
      times: ["Sundays 8:15 AM"],
      note: "Or by appointment with Father",
    },
    liturgy: [
      { day: "Sunday", time: "9:00 AM", language: "English & Ukrainian", label: "Divine Liturgy" },
      { day: "Sunday", time: "11:30 AM", language: "Ukrainian", label: "Divine Liturgy" },
    ],
    other: [
      { day: "Sunday", time: "8:30 AM", label: "Rosary", language: "English" },
      { day: "Sunday", time: "11:15 AM", label: "Divine Mercy Prayer", language: "Ukrainian" },
    ],
  },

  // Pastor
  pastor: {
    title: "Very Reverend",
    name: "Fr. Michael Lutsak",
    role: "Pastor",
    // photo: "/images/pastor.jpg", // uncomment when photo available
  },

  // Links
  links: {
    donate: null, // parish donation URL when available
    livestream: null, // YouTube/Facebook livestream URL
    bulletin: null, // URL to latest bulletin PDF or upload path
    newsletter: null, // Flocknote or mailing list URL
    facebook: null,
    youtube: null,
    instagram: null,
  },

  // Calendar API integration
  calendarApi: "https://evanr-web.github.io/calendar-api",

  // Language
  defaultLanguage: "en" as "en" | "uk",
  bilingual: true,

  // Design overrides (optional — defaults are beautiful)
  // Uncomment to override the template palette
  // colors: {
  //   primary: "#1A3A6B",
  //   accent: "#C9A84C",
  //   warm: "#9B2D30",
  // },
};

export type ParishConfig = typeof parish;
