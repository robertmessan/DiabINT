import streamlit as st

im2=Image.open("images/logo_MonMedecin.jpg")
im1=Image.open("data/diabetes_image.jpg")
st.set_page_config(page_title="Mes activités physiques",page_icon=im2, layout="wide")
html_temp = """
<div style="background-color:#748c08;padding:1.5px">
<h1 style="color:white;text-align:center;">10 Exercices pour les Diabétiques 🚴</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.header('1. La Marche')
st.markdown('Vous n\'avez pas besoin d\'un abonnement à une salle de sport ou d\'un équipement coûteux pour bouger.')
st.markdown('Si vous avez une paire de chaussures de soutien et un endroit sûr pour marcher, vous pouvez commencer dès aujourd\'hui. En fait, vous pouvez atteindre l\'objectif minimum recommandé pour la condition physique aérobie en faisant une marche rapide de 30 minutes cinq jours par semaine.')
st.markdown('Selon une étude réalisée en 2023, la marche peut aider les personnes atteintes de diabète de type 2 à réduire leur tension artérielle, leur taux de glycémie et leur indice de masse corporelle.')

st.header('2. Cyclisme')
st.markdown("Environ la moitié des personnes atteintes de diabète de type 2Trusted Source souffrent d'arthrite. Les deux maladies ont plusieurs facteurs de risque en commun, notamment l'obésité.")
st.markdown("La neuropathie diabétique, qui survient lorsque les nerfs sont endommagés, peut également provoquer des douleurs articulaires chez les personnes atteintes de diabète de type 2.")
st.markdown("Si vous souffrez de douleurs dans les articulations inférieures, envisagez d'opter pour des exercices à faible impact. Le vélo, par exemple, peut vous aider à atteindre vos objectifs de remise en forme tout en minimisant la pression sur vos articulations.")

st.header('3. Natation')
st.markdown("Les activités aquatiques constituent une autre option d'exercice respectueuse des articulations. Par exemple, la natation, l'aquagym, l'aquajogging et d'autres activités aquatiques peuvent faire travailler votre cœur, vos poumons et vos muscles, tout en sollicitant peu vos articulations.")
st.markdown("Une revue de 2017 a révélé que les exercices aquatiques peuvent aider à réduire le taux de sucre dans le sang, tout comme le font les exercices terrestres.")

st.header('4. Les sports d\'équipe')
st.markdown("Si vous avez du mal à vous motiver pour faire de l'exercice, il peut être utile de rejoindre une équipe de sport de loisir. La possibilité de socialiser avec vos coéquipiers et l'engagement que vous prenez envers eux peuvent vous aider à trouver la motivation dont vous avez besoin pour vous présenter chaque semaine.")
st.markdown("De nombreux sports récréatifs offrent un bon entraînement aérobique. Pensez à essayer le basket-ball, le football, le softball, le tennis en couple ou l'ultimate frisbee.")

st.header('5. Danse aérobique')
st.markdown("S'inscrire à un cours de danse aérobique ou à un autre cours de fitness peut également vous aider à atteindre vos objectifs en matière d'exercice physique. Par exemple, la Zumba est un programme de fitness qui combine la danse et les mouvements d'aérobic pour un entraînement rapide.")
st.markdown("Une étude de 2015, a montré que les femmes atteintes de diabète de type 2 étaient plus motivées pour faire de l'exercice après avoir participé à des cours de Zumba pendant 16 semaines. Les participantes ont également amélioré leur forme aérobique et perdu du poids.")

st.header('6. Haltérophilie')
st.markdown("L'haltérophilie et d'autres activités de renforcement aident à développer votre masse musculaire, ce qui peut augmenter le nombre de calories que vous brûlez chaque jour. Selon l'ADA, la musculation peut également contribuer à améliorer le contrôle de la glycémie.")
st.markdown("Si vous souhaitez intégrer l'haltérophilie à votre programme d'exercices hebdomadaire, vous pouvez utiliser des machines de musculation, des poids libres ou même des objets ménagers lourds, tels que des boîtes de conserve ou des bouteilles d'eau.")
st.markdown("Pour apprendre à soulever des poids de manière sûre et efficace, vous pouvez vous inscrire à un cours d'haltérophilie ou demander conseil à un entraîneur professionnel.")

st.header('7. Exercices avec bandes de résistance')
st.markdown("Les poids ne sont pas le seul outil que vous pouvez utiliser pour renforcer vos muscles. Vous pouvez également effectuer une grande variété d'activités de renforcement avec des bandes de résistance.")
st.markdown("Pour savoir comment les intégrer à vos séances d'entraînement, consultez un entraîneur professionnel, suivez un cours sur les bandes de résistance ou regardez une vidéo d'entraînement sur les bandes de résistance.")
st.markdown("En plus d'augmenter votre force, l'exercice avec des bandes de résistance peut apporter des avantages modestes à votre contrôle de la glycémie, selon une étude de 2018.")

st.header('8. La gymnastique suédoise')
st.markdown("En gymnastique suédoise, vous utilisez le poids de votre propre corps pour renforcer vos muscles. Les exercices de gymnastique suédoise les plus courants sont les pompes, les tractions, les accroupissements, les fentes et les abdominaux.")
st.markdown("Que vous choisissiez de renforcer vos muscles avec des poids, des bandes de résistance ou votre propre poids, essayez de faire travailler tous les principaux groupes musculaires de votre corps.")
st.markdown("Pour donner à votre corps le temps de récupérer, les experts suggèrent de prendre un jour de repos entre chaque séance de renforcement musculaire.")

st.header('9. Pilates')
st.markdown("Pilates est un programme de fitness populaire conçu pour améliorer la force centrale, la coordination et l'équilibre. Selon une étude réalisée en 2020 sur des femmes âgées atteintes de diabète de type 2, il pourrait également contribuer à améliorer le contrôle de la glycémie.")
st.markdown("Envisagez de vous inscrire à un cours de Pilates dans votre salle de sport locale ou dans un studio de Pilates. De nombreux livres et vidéos didactiques sont également disponibles.")

st.header('10. Yoga')
st.markdown("Selon une étude de 2016, le yoga peut aider les personnes atteintes de diabète de type 2 à gérer leur glycémie, leur taux de cholestérol et leur poids. Il peut également contribuer à réduire votre tension artérielle, à améliorer la qualité de votre sommeil et à stimuler votre humeur.")
#st.markdown("If you're interested in trying yoga, sign up for a class at a local studio or gym. Un professionnel qualifié peut vous aider à apprendre comment passer d'une pose à l'autre, en adoptant la bonne posture et la bonne technique de respiration.")

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")



st.markdown("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[Retourner sur la page d'accueil](https://voyag-int.rf.gd)\n\n\n\n")
st.markdown("\n\n\n\n\n[Kossi Robert MESSAN](https://www.linkedin.com/in/kossi-robert-messan-252954223/)")



