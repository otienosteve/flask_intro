from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def landingpage():
    return render_template("index.html")
    


@app.route("/aboutme")
def aboutme():
    return render_template("about.html")


@app.route("/personal")
def personal():
    return "<p>Jack Sparrow was a legendary pirate of the Seven Seas, and the irreverent trickster of the Caribbean. A captain of equally dubious morality and sobriety, a master of self-promotion and self-interest, Jack fought a constant and losing battle with his own best tendencies. Jack's first love was the sea, his second, his beloved ship the Black Pearl.The son of Captain Edward Teague, Jack Sparrow was born on a pirate ship in a typhoon. Before he was known as Captain Jack Sparrow, he was simply known as Jack, a teenage stowaway who, even then, had a desire for adventure. Jack first sailed on the Barnacle with a young ragtag crew on a quest to locate and procure the legendary Sword of Cortés. As a young pirate he earned the name Jack Sparrow when he trapped the notorious Spanish pirate hunter Capitán Salazar in the Devil's Triangle. Years after his teenage adventures, an encounter with the infamous rogue pirates forced him to abandon the pirate life and take employment in the East India Trading Company. After five years of faithful service, during which he sailed across all the Seven Seas, he was given command of the Wicked Wench, a ship owned by Cutler Beckett, the EITC Director for West Africa. As Beckett's employee, Jack searched for the mystical island of Kerma and its legendary treasure, until he decided to betray Beckett and keep the island and its inhabitants safe from Beckett and his slave traders. When Beckett contracted him to transport a cargo of slaves to the Bahamas, Jack chose to liberate them and steal the Wench from Beckett. However, Beckett's men managed to find him and branded him as a pirate, while the Wench was set aflame and sunk. After striking a bargain with Davy Jones, the ghostly captain of the Flying Dutchman, to resurrect his beloved vessel, Jack had the Wench renamed the Black Pearl and began the pirate life anew. At some point, Jack Sparrow became one of the nine Pirate Lords, his domain being the Caribbean Sea.Throughout his years as an infamous pirate of the Caribbean, Jack Sparrow embarked on many adventures, several of which involved gaining items of unique value. Jack was captain of the Black Pearl for two years, during which time he searched for the Shadow Gold. But when he was after the treasure of Isla de Muerta, Jack lost the Pearl in a mutiny led by his first mate, Captain Hector Barbossa. Ten years later, with the help of Will Turner and Elizabeth Swann, Jack retrieved the Black Pearl after having fought and killed the cursed Barbossa, thereby becoming its captain once again. Jack was soon after the Dead Man's Chest, to settle his debt with the fearsome Davy Jones, which ended with him being taken to Davy Jones' Locker by the Kraken. After escaping the Locker with the help of his crew, led by the resurrected Hector Barbossa, Jack had joined with the Brethren Court in the battle against Lord Cutler Beckett, who had control over Davy Jones and the Flying Dutchman. Jack would later sail on stranger tides during the quest for the Fountain of Youth, contending with the notorious Blackbeard and his daughter, Angelica, who forced him aboard the Queen Anne's Revenge. After the malicious Captain Salazar's ghost crew escaped from the Devil's Triangle bent on killing every pirate, Jack sought to reverse his recent spate of ill fortune by finding the Trident of Poseidon. Jack would be helped on his journey by Henry Turner who sought to free his father and they would be aided by Carina Smyth.Over the course of time, Captain Jack Sparrow became a center of intrigue as myths and legends have been told of his exploits. Most of these tales, however, were exaggerations, or even fabrications, embellished by Jack himself to bolster his reputation. Despite his dishonesty and many deceptions, Jack Sparrow did embark on a number of grand and thrilling adventures, some involving the supernatural, pirate lore, magic, and journeys in discovering hidden treasures. Indeed, Jack's ultimate ambition was to have the freedom to sail the seas as a legendary pirate for eternity.</p>"

@app.route("/contact")
def contact():
    return "<h4>Pirates Land - One eye is Watching<h4>"

if __name__ =='__main__':
    app.run(debug=1)